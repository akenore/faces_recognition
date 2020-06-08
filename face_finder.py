import faces_recognition

image = faces_recognition.load_image_file('img/groups/team1.jpg')
face_locations = faces_recognition.face_locations(image)


print(f'There are {len(face_locations)}people in this image')