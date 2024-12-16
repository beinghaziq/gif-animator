# import cv2
# import imageio
# import numpy as np

# def animated_overlay_in_gif(gif_path, overlay_path, output_path, start_position=(0, 0), end_position=(100, 100), overlay_size=None):
#     """
#     Add an animated overlay to a GIF, moving from start_position to end_position.

#     Args:
#     - gif_path (str): Path to the original GIF file.
#     - overlay_path (str): Path to the overlay image.
#     - output_path (str): Path to save the modified GIF.
#     - start_position (tuple): Starting (x, y) position of the overlay.
#     - end_position (tuple): Ending (x, y) position of the overlay.
#     - overlay_size (tuple): (width, height) to resize the overlay; use None to keep the original size.
#     """
#     # Load the overlay image with alpha channel support
#     overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
#     if overlay_size:
#         overlay = cv2.resize(overlay, overlay_size)

#     # Calculate movement increments per frame
#     gif_reader = imageio.get_reader(gif_path)
#     gif_meta = gif_reader.get_meta_data()
#     num_frames = sum(1 for _ in gif_reader)  # Count frames by iterating
#     x_start, y_start = start_position
#     x_end, y_end = end_position
#     x_step = (x_end - x_start) / num_frames
#     y_step = (y_end - y_start) / num_frames

#     modified_frames = []

#     # Process each frame with the overlay moving from start to end position
#     for i, frame in enumerate(gif_reader):
#         # Compute overlay position for this frame
#         x = int(x_start + i * x_step)
#         y = int(y_start + i * y_step)

#         # Convert the GIF frame to BGRA for OpenCV
#         frame_bgr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGBA2BGRA)

#         # Get overlay dimensions
#         h, w = overlay.shape[:2]

#         # Ensure overlay fits within the frame at this position
#         if x + w > frame_bgr.shape[1] or y + h > frame_bgr.shape[0]:
#             continue  # Skip frames where overlay would exceed bounds

#         # Extract the region of interest (ROI) where overlay will be placed
#         roi = frame_bgr[y:y+h, x:x+w]

#         # Alpha blending if overlay has an alpha channel
#         if overlay.shape[2] == 4:  # Check if overlay has an alpha channel
#             alpha_overlay = overlay[:, :, 3] / 255.0
#             alpha_frame = 1.0 - alpha_overlay

#             for c in range(3):  # Blend each color channel
#                 roi[:, :, c] = (
#                     alpha_overlay * overlay[:, :, c] +
#                     alpha_frame * roi[:, :, c]
#                 )
#         else:
#             roi[:, :, :3] = overlay[:, :, :3]

#         # Place the modified ROI back into the frame
#         frame_bgr[y:y+h, x:x+w] = roi

#         # Convert the frame back to RGBA for GIF saving
#         frame_rgba = cv2.cvtColor(frame_bgr, cv2.COLOR_BGRA2RGBA)
#         modified_frames.append(frame_rgba)

#     # Save the modified frames as a new GIF with original metadata
#     imageio.mimsave(output_path, modified_frames, duration=gif_meta['duration'] / 1000, loop=gif_meta.get('loop', 0))

# # Example usage with animated overlay moving from (0,0) to (200,200)
# # animated_overlay_in_gif("input.gif", "overlay.png", "output_animated_overlay.gif", start_position=(0, 0), end_position=(200, 200), overlay_size=(100, 100))


# # Example usage
# # Position (50, 50) and overlay resized to (100, 100)
# animated_overlay_in_gif("input.gif", "overlay.jpg", "output_filled_a.gif", start_position=(100, 100),end_position=(500, 320), overlay_size=(300, 530))











# import cv2
# import imageio
# import numpy as np
# import random

# def vibrate_overlay_in_gif(gif_path, overlay_path, output_path, base_position=(50, 50), overlay_size=None, vibrate_range=5):
#     """
#     Add a vibrating overlay effect to a GIF by applying random small shifts to the overlay position in each frame.

#     Args:
#     - gif_path (str): Path to the original GIF file.
#     - overlay_path (str): Path to the overlay image.
#     - output_path (str): Path to save the modified GIF.
#     - base_position (tuple): Base (x, y) position of the overlay.
#     - overlay_size (tuple): (width, height) to resize the overlay; use None to keep the original size.
#     - vibrate_range (int): Maximum number of pixels to shift the overlay in any direction per frame.
#     """
#     # Load the overlay image with alpha channel support
#     overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
#     if overlay_size:
#         overlay = cv2.resize(overlay, overlay_size)

#     # Read the GIF frames
#     gif_reader = imageio.get_reader(gif_path)
#     gif_meta = gif_reader.get_meta_data()
#     modified_frames = []

#     # Process each frame and apply vibration effect
#     for frame in gif_reader:
#         # Generate a random offset within the specified vibrate range
#         x_offset = random.randint(-vibrate_range, vibrate_range)
#         y_offset = random.randint(-vibrate_range, vibrate_range)
        
#         # Calculate the overlay position for this frame
#         x = base_position[0] + x_offset
#         y = base_position[1] + y_offset

#         # Convert the GIF frame to BGRA for OpenCV
#         frame_bgr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGBA2BGRA)

#         # Get overlay dimensions
#         h, w = overlay.shape[:2]

#         # Ensure overlay fits within the frame at this position
#         if x + w > frame_bgr.shape[1] or y + h > frame_bgr.shape[0] or x < 0 or y < 0:
#             continue  # Skip frames where overlay would exceed bounds

#         # Extract the region of interest (ROI) where overlay will be applied
#         roi = frame_bgr[y:y+h, x:x+w]

#         # Alpha blending if overlay has an alpha channel
#         if overlay.shape[2] == 4:  # Check if overlay has an alpha channel
#             alpha_overlay = overlay[:, :, 3] / 255.0
#             alpha_frame = 1.0 - alpha_overlay

#             for c in range(3):  # Blend each color channel
#                 roi[:, :, c] = (
#                     alpha_overlay * overlay[:, :, c] +
#                     alpha_frame * roi[:, :, c]
#                 )
#         else:
#             roi[:, :, :3] = overlay[:, :, :3]

#         # Place the modified ROI back into the frame
#         frame_bgr[y:y+h, x:x+w] = roi

#         # Convert the frame back to RGBA for GIF saving
#         frame_rgba = cv2.cvtColor(frame_bgr, cv2.COLOR_BGRA2RGBA)
#         modified_frames.append(frame_rgba)

#     # Save the modified frames as a new GIF with original metadata
#     imageio.mimsave(output_path, modified_frames, duration=gif_meta['duration'] / 1000, loop=gif_meta.get('loop', 0))

# # Example usage with vibrate effect
# vibrate_overlay_in_gif("input.gif", "overlay.jpg", "output_vibrate_overlay.gif", base_position=(500, 320), overlay_size=(300, 530), vibrate_range=1)

# # animated_overlay_in_gif("input.gif", "overlay.jpg", "output_filled_a.gif", start_position=(100, 100),end_position=(500, 320), overlay_size=(300, 530))




















import cv2
import numpy as np
import imageio
import os

def fade_in_overlay_in_gif(gif_path, overlay_path, output_path, base_position=(50, 50), overlay_size=None, fade_duration=20):
    """
    Add a fade-in effect to a JPG overlay image in a GIF. The overlay gradually becomes more visible over `fade_duration` frames.
    """
    # Ensure that the input files exist
    if not os.path.exists(gif_path):
        raise FileNotFoundError(f"GIF file not found: {gif_path}")
    if not os.path.exists(overlay_path):
        raise FileNotFoundError(f"Overlay image file not found: {overlay_path}")

    # Load the JPG image (it does not have an alpha channel)
    overlay = cv2.imread(overlay_path)
    if overlay is None:
        raise ValueError(f"Failed to load overlay image from {overlay_path}")

    # Convert JPG image to RGBA (add an alpha channel with full transparency)
    overlay_rgba = cv2.cvtColor(overlay, cv2.COLOR_BGR2BGRA)
    overlay_rgba[:, :, 3] = 0  # Set alpha channel to 0 (fully transparent)

    # Resize overlay if needed
    if overlay_size:
        overlay_rgba = cv2.resize(overlay_rgba, overlay_size)

    # Read the GIF frames
    gif_reader = imageio.get_reader(gif_path)
    gif_meta = gif_reader.get_meta_data()
    modified_frames = []

    # Loop through each frame of the GIF
    for i, frame in enumerate(gif_reader):
        # Calculate the fade-in factor (0 to 1) based on the current frame number
        fade_factor = min(1.0, i / fade_duration)

        # Convert the GIF frame to BGRA for easier handling with OpenCV
        frame_bgr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGBA2BGRA)

        # Get the dimensions of the overlay
        overlay_height, overlay_width = overlay_rgba.shape[:2]

        # Calculate the position to place the overlay
        x, y = base_position

        # Make sure the overlay fits inside the frame
        if x + overlay_width > frame_bgr.shape[1] or y + overlay_height > frame_bgr.shape[0]:
            continue  # Skip if the overlay won't fit in the frame

        # Extract the region of interest (ROI) where the overlay will be placed
        roi = frame_bgr[y:y+overlay_height, x:x+overlay_width]

        # Split the overlay into its color channels and alpha channel
        overlay_rgb = overlay_rgba[:, :, :3]  # RGB channels
        overlay_alpha = overlay_rgba[:, :, 3] / 255.0  # Normalize the alpha channel to 0-1

        # Apply the fade-in effect by scaling the alpha channel
        overlay_alpha = overlay_alpha * fade_factor

        # Iterate over each pixel in the overlay and apply alpha blending to the frame
        for c in range(3):  # Iterate over RGB channels
            # Blending formula: new_pixel = (1 - alpha) * background_pixel + alpha * overlay_pixel
            roi[:, :, c] = (1 - overlay_alpha) * roi[:, :, c] + overlay_alpha * overlay_rgb[:, :, c]

        # Place the modified ROI back into the frame
        frame_bgr[y:y+overlay_height, x:x+overlay_width] = roi

        # Convert the frame back to RGBA for saving as a GIF
        frame_rgba = cv2.cvtColor(frame_bgr, cv2.COLOR_BGRA2RGBA)
        modified_frames.append(frame_rgba)

    # Save the modified frames as a new GIF
    imageio.mimsave(output_path, modified_frames, duration=gif_meta['duration'] / 1000, loop=gif_meta.get('loop', 0))

    print(f"GIF saved to {output_path}")




fade_in_overlay_in_gif("input.gif", "overlay.jpg", "output_fade_in_overlay.gif", base_position=(500, 320), overlay_size=(300, 530), fade_duration=30)


# animated_overlay_in_gif("input.gif", "overlay.jpg", "output_filled_a.gif", start_position=(100, 100),end_position=(500, 320), overlay_size=(300, 530))
# num_frames = sum(1 for _ in gif_reader)  # Count frames by iterating
# 