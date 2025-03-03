from PIL import Image
import sys
import argparse

def resize_gif(input_path, output_path, scale):
    with Image.open(input_path) as img:
        frames = []
        for frame in range(0, img.n_frames):
            img.seek(frame)
            frame_image = img.copy()
            frame_image = frame_image.resize(
                (int(frame_image.width * scale), int(frame_image.height * scale)),
                Image.LANCZOS
            )
            frames.append(frame_image)

        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=img.info['loop'],
            duration=img.info['duration'],
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize a GIF by a scale factor.")
    parser.add_argument("-in", "--input_gif", required=True, help="Path to the input GIF file")
    parser.add_argument("-s", "--scale_factor", type=float, default=0.5, help="Scale factor to resize the GIF (default: 0.5)")

    args = parser.parse_args()

    input_gif = args.input_gif
    output_gif = input_gif.replace(".gif", f"_resized_{args.scale_factor}.gif")
    scale_factor = args.scale_factor

    resize_gif(input_gif, output_gif, scale_factor)