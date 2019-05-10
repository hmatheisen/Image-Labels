from dotenv import load_dotenv
from labels import ImageLabels

# Load .env variables
load_dotenv()

# Fetch images
labels = ImageLabels()
images = labels.fetch_images().json()["images"]

for image in images:
    # Fetch image details
    image_details = labels.fetch_image_details(image["image_id"]).json()
    # Create backup
    labels.create_file("images/", image_details)
    # Update Training Data
    response = labels.update_training_data(image_details)

    print(response.json())

    # Fetch the new details
    new_image_details = labels.fetch_image_details(image["image_id"]).json()
    # Create files again
    labels.create_file("new_images/", new_image_details)
