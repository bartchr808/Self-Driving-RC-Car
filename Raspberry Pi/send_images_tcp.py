import io, time, picamera
from PIL import Image
import socket, struct

# Performs the continuous image capturing using a UDPServer object to send it
def capture_images():
    client_socket = socket.socket()
    client_socket.connect(("192.168.1.41", 8000))
    client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    # Make a file-like object out of the connection
    connection = client_socket.makefile('wb')
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (480, 360)
            # Start a preview and let the camera warm up for 2 seconds
            camera.start_preview()
            time.sleep(2)
            
            start = time.time()
            
            # Construct a stream to hold image data temporarily
            stream = io.BytesIO()
            
            for foo in camera.capture_continuous(stream, 'jpeg'):
                
                # Write the length of the capture to the stream and flush to
                # ensure it actually gets sent
                connection.write(struct.pack('<L', stream.tell()))
                connection.flush()

                # Rewind the stream and send the image data over the wire
                stream.seek(0)
                connection.write(stream.read())
                
                # If we've been capturing for more than 30 seconds, quit
                if time.time() - start > 30:
                    break
                
                # Reset the stream for the next capture
                stream.seek(0)
                stream.truncate()
        
        # Write a length of zero to the stream to signal we're done
        connection.write(struct.pack('<L', 0))
    
    finally:
        connection.close()
        client_socket.close()


if __name__ == "__main__":
    capture_images()
