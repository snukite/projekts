import tkinter as tk
from PIL import Image, ImageTk

def paradit_tirdzniecibas_skatu():
    sakuma_skats.pack_forget()  
    tirdzniecibas_skats.pack(fill='both', expand=True)

def lokacijas_poga():
    tirdzniecibas_skats.pack_forget()
    lokacijas_skats.pack(fill='both', expand=True)

def instrukcijas_poga():
    print("Instrukcijas poga nospiesta!")

def norekinasanas_poga():
    print("Norēķināšanās poga nospiesta!")

def atpakal():
    lokacijas_skats.pack_forget()
    tirdzniecibas_skats.pack(fill='both', expand=True)

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
tirdzniecibas_teksts.pack(pady=50, padx=30, anchor="e")

lokacijas_poga = tk.Button(tirdzniecibas_skats, text="FISHING24-7 tirdzniecības automātu lokācijas", font=("Verdana", 14), fg="#b90843", bg="white", command=lokacijas_poga)
lokacijas_poga.pack(pady=(30), anchor="e", padx=100) 

instrukcijas_poga = tk.Button(tirdzniecibas_skats, text="Lietošanas instrukcija", font=("Verdana", 14), fg="#b90843", bg="white", command=instrukcijas_poga)
instrukcijas_poga.pack(pady=(30), anchor="e", padx=335) 

norekinasanas_poga = tk.Button(tirdzniecibas_skats, text="Iespējamie norēķināšanās veidi", font=("Verdana", 14), fg="#b90843", bg="white", command=norekinasanas_poga)
norekinasanas_poga.pack(pady=(30), anchor="e", padx=240) 

lokacijas_skats = tk.Frame(window, bg="#c0d099")

lokacijas_virsraksts = tk.Label(lokacijas_skats, text="FISHING24-7 tirdzniecības automātu lokācijas", font=("Verdana", 18, "bold"), fg="#b90843", bg="#c0d099")
lokacijas_virsraksts.grid(row=0, column=0, columnspan=2, pady=10)

lokacijas_teksts1 = tk.Label(lokacijas_skats, text="1. Siguldā, Strēlnieku ielā 2 - T/C Šokolāde ēkas ziemeļu pusē, pie B ieejas", 
font=("Verdana", 12), 
fg="black", 
bg="#c0d099", 
wraplength=500, justify="left", anchor="w")
lokacijas_teksts1.grid(row=1, column=0, padx=30, pady=1, sticky="w")

image_path = "sigulda.png" 
image = Image.open(image_path).resize((400, 135))  
photo = ImageTk.PhotoImage(image)
lokacijas_attels = tk.Label(lokacijas_skats, image=photo, bg="#c0d099")
lokacijas_attels.grid(row=2, column=0, padx=30, pady=1, sticky="w")

lokacijas_teksts2 = tk.Label(lokacijas_skats, text="2. Rīgā, Brīvības gatvē 404 - pa kreisi no veikala \"Mini Rimi\" ieejas, blakus Omniva pakomātam ", 
font=("Verdana", 12), 
fg="black", 
bg="#c0d099", 
wraplength=500, justify="left", anchor="w")
lokacijas_teksts2.grid(row=3, column=0, padx=30, pady=1, sticky="w")

image_path2 = "brivibas.png" 
image2 = Image.open(image_path2).resize((400, 135))  
photo2 = ImageTk.PhotoImage(image2)
lokacijas_attels2 = tk.Label(lokacijas_skats, image=photo2, bg="#c0d099")
lokacijas_attels2.grid(row=4, column=0, padx=30, pady=1, sticky="w")

lokacijas_teksts3 = tk.Label(lokacijas_skats, text="3. Rīgā, Vaidavas ielā 9B - pa kreisi no veikala \"Mini Rimi\" ieejas, blakus Omniva pakomātam ", 
font=("Verdana", 12), 
fg="black", 
bg="#c0d099", 
wraplength=500, justify="left", anchor="w")
lokacijas_teksts3.grid(row=5, column=0, padx=30, pady=10, sticky="w")

image_path3 = "vaidavas.png" 
image3 = Image.open(image_path3).resize((400, 135))  
photo3 = ImageTk.PhotoImage(image3)
lokacijas_attels3 = tk.Label(lokacijas_skats, image=photo3, bg="#c0d099")
lokacijas_attels3.grid(row=6, column=0, padx=30, pady=1, sticky="w")

lokacijas_teksts4 = tk.Label(lokacijas_skats, text="4. Rīgā, Latgales ielā 256B - pa kreisi no veikala \"Mini Rimi\" ieejas, blakus Omniva pakomātam", 
font=("Verdana", 12), 
fg="black", 
bg="#c0d099", 
wraplength=500, justify="left", anchor="w")
lokacijas_teksts4.grid(row=1, column=1, padx=30, pady=10, sticky="w")

image_path4 = "latgales.png" 
image4 = Image.open(image_path4).resize((400, 135))  
photo4 = ImageTk.PhotoImage(image4)
lokacijas_attels4 = tk.Label(lokacijas_skats, image=photo4, bg="#c0d099")
lokacijas_attels4.grid(row=2, column=1, padx=30, pady=1, sticky="w")

lokacijas_teksts5 = tk.Label(lokacijas_skats, text="5. Rīgā, Kalnciema ielā 41 - pa labi no veikala \"Mini Rimi\" ieejas, blakus SEB bankomātam", 
font=("Verdana", 12), 
fg="black", 
bg="#c0d099", 
wraplength=500, justify="left", anchor="w")
lokacijas_teksts5.grid(row=3, column=1, padx=30, pady=10, sticky="w")

image_path5 = "kalnciema.png" 
image5 = Image.open(image_path5).resize((400, 135))  
photo5 = ImageTk.PhotoImage(image5)
lokacijas_attels5 = tk.Label(lokacijas_skats, image=photo5, bg="#c0d099")
lokacijas_attels5.grid(row=4, column=1, padx=30, pady=1, sticky="w")

atpakal_poga = tk.Button(lokacijas_skats, text="Atpakaļ", font=("Verdana", 14), fg="#b90843", bg="white", command=atpakal)
atpakal_poga.grid(row=6, column=1, sticky="se")

window.mainloop()
