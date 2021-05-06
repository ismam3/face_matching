from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
import face_recognition
import threading
import dlib
import face_recognition_models


def clicked(sr):
    filename = filedialog.askopenfilename(title="Browse images", filetypes=(("JPG Image", "*.jpg"), ("PNG Image", ".png")))
    if sr == "first":
        first_image_location.set(filename)
    else:
        second_image_location.set(filename)

window = Tk()
window.iconbitmap('E:/ML/face_mask/pyt/icn.ico')
window.geometry("500x500+300+100")  # setting up geometry property of window
window.resizable(0, 0)  # window can't be resized
window.title("Face Matching Application")  # setting a title
window.configure(bg="pink")
second_image_location = StringVar()
first_image_location = StringVar()
face_result = StringVar()
similarity = StringVar()
threads = []
results = []
dlib.shape_predictor("E:/ML/face_mask/pyt/face_recognition_models/models/shape_predictor_68_face_landmarks.dat")

result_frame = LabelFrame(window, text="Result Section", relief=SUNKEN)
face_result_label = Label(result_frame)
progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode="indeterminate")


def result():
    try:
        face_result_label.configure(text="")
        trainImg = face_recognition.load_image_file(first_image_location.get())
        trainImg = cv2.cvtColor(trainImg, cv2.COLOR_BGR2RGB)
        testImg = face_recognition.load_image_file(second_image_location.get())
        testImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2RGB)

        faceLoc = face_recognition.face_locations(trainImg)[0]
        encodeTrain = face_recognition.face_encodings(trainImg)[0]
        cv2.rectangle(trainImg, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 3)

        faceLoc_test = face_recognition.face_locations(testImg)[0]
        encode_test = face_recognition.face_encodings(testImg)[0]
        cv2.rectangle(testImg, (faceLoc_test[3], faceLoc_test[0]), (faceLoc_test[1], faceLoc_test[2]), (255, 0, 0), 3)

        face_result.set(face_recognition.compare_faces([encodeTrain], encode_test)[0])
        distance = 1 - face_recognition.face_distance([encodeTrain], encode_test)[0]
        similarity.set(distance * 100)

        results.append(f'Are the faces the same??? {"Yes" if face_result.get()== "True" else "No"}\nSimilarity: {similarity.get()} %')


    except:
        results.append("লাভ নাই! আগে মুখের ছবি দেন!\n Please select a picture with face")


def get_result():
    progress_bar.start(5)
    result()
    progress_bar.stop()
    face_result_label.configure(text=results[-1])


def thread_append():
    t = threading.Thread(target=get_result)
    threads.append(t)
    last_thread = threads[-1]
    last_thread.start()
    results.append("")

def preview(sr):
    try:
        image = cv2.imread(first_image_location.get() if sr == "first" else second_image_location.get())
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        faceLoc = face_recognition.face_locations(image)[0]
        cv2.rectangle(image, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0), 5)
        resized = cv2.resize(image, (300, 300))
        cv2.imshow(f'{"First image " if sr == "first" else "Second image "} - [{first_image_location.get() if sr == "first" else second_image_location.get()}]',resized)
    except:
        results.append("লাভ নাই! আগে মুখের ছবি দেন!\n Please select a picture with face")


image_browser = LabelFrame(window,text="Browse your images",relief=GROOVE)
firstImage_frame = Frame(image_browser)
secondImage_frame = Frame(image_browser)
first_button = Frame(firstImage_frame)
second_button = Frame(secondImage_frame)

Label(firstImage_frame,text="First Image:").pack(side=LEFT)
Entry(firstImage_frame, textvariable=first_image_location,relief=GROOVE).pack(side=LEFT,expand=True,fill=X)
Button(first_button,text="Preview",command=lambda:preview("first")).pack(side=RIGHT,padx=5)
Button(first_button,text="Browse",command=lambda:clicked("first")).pack(side=LEFT)
Label(secondImage_frame, text="Second Image:").pack(side=LEFT)
Entry(secondImage_frame, textvariable=second_image_location, relief=GROOVE).pack(side=LEFT,expand=True, fill=X)
Button(second_button,text="Preview",command=lambda:preview("second")).pack(side=RIGHT,padx=5)
Button(second_button,text="Browse",command=lambda:clicked("second")).pack(side=LEFT)

first_button.pack()
second_button.pack()
firstImage_frame.pack(padx=5, pady=5, expand=True,fill=X)
secondImage_frame.pack(padx=5, pady=5, expand=True,fill=X)
image_browser.pack(padx=5, pady=30, fill=X)

Button(window,text="Compare",command=thread_append,relief=RAISED,bg='blue',fg='white').pack(pady=50, padx=15, fill=X)

face_result_label.pack()
result_frame.pack(pady=50,padx=5,fill=X)
progress_bar.pack()

window.mainloop()
cv2.waitKey(0)
cv2.destroyAllWindows()
