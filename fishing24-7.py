import tkinter as tk
from PIL import Image, ImageTk

def paradit_tirdzniecibas_skatu():
    sakuma_skats.pack_forget()  # Paslēpj sākuma skatu
    tirdzniecibas_skats.pack(fill='both', expand=True)

def lokacijas_poga():
    print("Lokācijas poga nospiesta!")

window = tk.Tk()
window.title("Informatīvā programma FISHING24-7 tirdzniecības automātiem")
window.geometry("1150x700")
window.resizable(False, False)
window.configure(bg="#c0d099")

sakuma_skats = tk.Frame(window,bg="#c0d099")
sakuma_skats.pack(fill='both', expand=True)
uzraksts = tk.Label(sakuma_skats, text="FISHING24-7", font=("Verdana", 30, "bold"), fg="#b90843", bg="#c0d099")
uzraksts.pack(pady=30)

original_image = Image.open("automats.png")
resized_image = original_image.resize((270, 400)) 
button_image = ImageTk.PhotoImage(resized_image)

image_button = tk.Button(sakuma_skats, image=button_image, borderwidth=0, bg="#c0d099", activebackground="#c0d099", command=paradit_tirdzniecibas_skatu)
image_button.pack(pady=30)

teksts_zem_pogas = tk.Label(sakuma_skats, text="Klikšķini uz tirdzniecības automāta, lai sāktu", font=("Verdana", 16), fg="#b90843", bg="#c0d099")
teksts_zem_pogas.pack(pady=10)

tirdzniecibas_skats = tk.Frame(window, bg="#c0d099")

tirdzniecibas_teksts = tk.Label(tirdzniecibas_skats, text="Tirdzniecības automātā 24/7 režīmā var iegādāties dažādas preces makšķerēšanai - zivju barības, dzīvās ēsmas, sausās un šķidrās piedevas, makšķerēšanas piederumus u.tml.\n\nTirdzniecības automāti atrodas ārpus telpām, tajos ievietotās preces ir marķētas un tiek uzglabātas temperatūrā no +2C līdz +5C.", 
font=("Verdana", 14), 
fg="#b90843", 
bg="#c0d099", 
wraplength=600, justify="left", anchor="e")
tirdzniecibas_teksts.pack(pady=30, padx=30, anchor="e")

lokacijas_poga = tk.Button(tirdzniecibas_skats, text="FISHING24-7 tirdzniecības automātu lokācijas", font=("Verdana", 12), fg="#b90843", bg="white", command=lokacijas_poga)
lokacijas_poga.pack(pady=(0, 20), anchor="e", padx=100) 

window.mainloop()