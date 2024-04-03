import Metashape

def process_images_to_point_cloud(image_folder, output_path):
    # Create a new Metashape document
    doc = Metashape.Document()

    # Create a new chunk
    chunk = doc.addChunk()
    chunk.label = "My Chunk"

    # Add photos to the chunk
    image_paths = Metashape.app.getFilenames("Select images", image_folder)
    chunk.addPhotos(image_paths)

    # Align photos
    chunk.matchPhotos(accuracy=Metashape.HighAccuracy, preselection=Metashape.GenericPreselection)
    chunk.alignCameras()

    # Build dense cloud
    chunk.buildDenseCloud(quality=Metashape.MediumQuality, depth_filtering=Metashape.AggressiveFiltering)

    # Export the dense cloud
    chunk.exportPoints(path=output_path, format=Metashape.PointsFormatLAS, dense_cloud=True)

    # Optionally: Save the project
    doc.save(path="path/to/your/project.msp")

# Example usage
image_folder = "path/to/your/images"
output_path = "path/to/your/output.las"
process_images_to_point_cloud(image_folder, output_path)
