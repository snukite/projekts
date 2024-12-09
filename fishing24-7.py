import tkinter as tk
from PIL import Image, ImageTk

def paradit_tirdzniecibas_skatu():
    sakuma_skats.pack_forget()  
    tirdzniecibas_skats.pack(fill='both', expand=True)

def plaukta_pogas():
    print("Poga uz attēla nospiesta!")

def lokacijas_poga():
    tirdzniecibas_skats.pack_forget()
    lokacijas_skats.pack(fill='both', expand=True)

def instrukcijas_poga():
    instrukcijas_logs = tk.Toplevel(window)
    instrukcijas_logs.title("Lietošanas instrukcija")
    instrukcijas_logs.geometry("453x640")
    instrukcijas_logs.resizable(False, False)
    instrukcijas_logs.configure(bg="#c0d099")

    instrukcijas_attels_path = "instrukcija.png" 
    instrukcijas_image = Image.open(instrukcijas_attels_path)
    instrukcijas_photo = ImageTk.PhotoImage(instrukcijas_image)

    attels_label = tk.Label(instrukcijas_logs, image=instrukcijas_photo, bg="#c0d099")
    attels_label.image = instrukcijas_photo  
    attels_label.pack()

    aizvert_poga = tk.Button(instrukcijas_logs, text="Aizvērt", font=("Verdana", 14), fg="#b90843", bg="white", borderwidth=0, command=instrukcijas_logs.destroy)
    aizvert_poga.place(x=330, y=580)

def norekinasanas_poga():
    norekinasanas_logs = tk.Toplevel(window)
    norekinasanas_logs.title("Norēķināšanās veidi")
    norekinasanas_logs.geometry("872x491")
    norekinasanas_logs.resizable(False, False)
    norekinasanas_logs.configure(bg="#c0d099")

    norekinasanas_attels_path = "norekinasanas.png" 
    norekinasanas_image = Image.open(norekinasanas_attels_path)
    norekinasanas_photo = ImageTk.PhotoImage(norekinasanas_image)

    attels_label2 = tk.Label(norekinasanas_logs, image=norekinasanas_photo, bg="#c0d099")
    attels_label2.image = norekinasanas_photo  
    attels_label2.pack()

    aizvert_poga = tk.Button(norekinasanas_logs, text="Aizvērt", font=("Verdana", 14), fg="#b90843", bg="white", borderwidth=2, command=norekinasanas_logs.destroy)
    aizvert_poga.place(x=755, y=430)

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
uzraksts.pack(pady=20)

original_image = Image.open("automats.png")
resized_image = original_image.resize((324, 480)) 
button_image = ImageTk.PhotoImage(resized_image)

image_button = tk.Button(sakuma_skats, image=button_image, borderwidth=0, bg="#c0d099", activebackground="#c0d099", command=paradit_tirdzniecibas_skatu)
image_button.pack(pady=5)

teksts_zem_pogas = tk.Label(sakuma_skats, text="Klikšķini uz tirdzniecības automāta, lai sāktu", font=("Verdana", 16), fg="#b90843", bg="#c0d099")
teksts_zem_pogas.pack(pady=10)

tirdzniecibas_skats = tk.Frame(window, bg="#c0d099")

tirdzniecibas_teksts = tk.Label(tirdzniecibas_skats, text="Tirdzniecības automātā 24/7 režīmā var iegādāties dažādas preces makšķerēšanai - zivju barības, dzīvās ēsmas, sausās un šķidrās piedevas, makšķerēšanas piederumus u.tml.\n\nTirdzniecības automāti atrodas ārpus telpām, tajos ievietotās preces ir marķētas un tiek uzglabātas temperatūrā no +2C līdz +5C.", 
font=("Verdana", 14), 
fg="#b90843", 
bg="#c0d099", 
wraplength=600, justify="left", anchor="e")
tirdzniecibas_teksts.pack(pady=50, padx=30, anchor="e")

tirdzniecibas_attels_path = "plaukti.png"  
original_image = Image.open(tirdzniecibas_attels_path)
resized_image = original_image.resize((488, 635))  
tirdzniecibas_photo = ImageTk.PhotoImage(resized_image)

tirdzniecibas_attels_label = tk.Label(tirdzniecibas_skats, image=tirdzniecibas_photo, bg="#c0d099")
tirdzniecibas_attels_label.image = tirdzniecibas_photo
tirdzniecibas_attels_label.place(x=20, y=30) 

def paradit_plaukta_saturu(attels_path, nosaukums, cena):
    
    tirdzniecibas_skats.pack_forget()

    plaukta_skats = tk.Frame(window, bg="#c0d099")
    plaukta_skats.pack(fill='both', expand=True)

    plaukta_frame = tk.Frame(plaukta_skats, bg="#c0d099")
    plaukta_frame.pack(pady=20)

    attels_image = Image.open(attels_path).resize((350, 600))  
    attels_photo = ImageTk.PhotoImage(attels_image)
    attels_label = tk.Label(plaukta_frame, image=attels_photo, bg="#c0d099")
    attels_label.image = attels_photo
    attels_label.pack(side="left", padx=20)

    informacija_frame = tk.Frame(plaukta_frame, bg="#c0d099")
    informacija_frame.pack(side="left", padx=20)

    nosaukums_label = tk.Label(informacija_frame, text=nosaukums, font=("Verdana", 24, "bold"), fg="#b90843", bg="#c0d099")
    nosaukums_label.pack(anchor="w")

    cena_label = tk.Label(informacija_frame, text=f"Cena: {cena}€", font=("Verdana", 18), fg="#b90843", bg="#c0d099")
    cena_label.pack(anchor="w", pady=50)

    atpakal_poga = tk.Button(plaukta_skats, text="Atpakaļ", font=("Verdana", 16), fg="#b90843", bg="white", borderwidth=0, command=lambda: [plaukta_skats.pack_forget(), tirdzniecibas_skats.pack(fill='both', expand=True)])
    atpakal_poga.place(x=1000, y=620)

def izveidot_attelu_pogu(skats, x, y, attela_nosaukums, komanda):
    original_image = Image.open(attela_nosaukums)
    resized_image = original_image.resize((28, 48))  
    button_image = ImageTk.PhotoImage(resized_image)
    poga = tk.Button(skats, image=button_image, borderwidth=0, bg="#e8e8e8", command=komanda)
    poga.image = button_image  
    poga.place(x=x, y=y)

def izveidot_attelu_pogu2(skats, x, y, attela_nosaukums, komanda):
    original_image = Image.open(attela_nosaukums)
    resized_image = original_image.resize((20, 34))  
    button_image = ImageTk.PhotoImage(resized_image)
    poga = tk.Button(skats, image=button_image, borderwidth=0, bg="#e8e8e8", command=komanda)
    poga.image = button_image  
    poga.place(x=x, y=y)

def izveidot_attelu_pogu3(skats, x, y, attela_nosaukums, komanda):
    original_image = Image.open(attela_nosaukums)
    resized_image = original_image.resize((19, 31))  
    button_image = ImageTk.PhotoImage(resized_image)
    poga = tk.Button(skats, image=button_image, borderwidth=0, bg="#e8e8e8", command=komanda)
    poga.image = button_image  
    poga.place(x=x, y=y)

izveidot_attelu_pogu(tirdzniecibas_skats, 85, 75, "bigcarp_kuku.png", lambda: paradit_plaukta_saturu("bigcarp_kuku.png", "Big Carp Kukurūza", "4.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 150, 75, "bigcarp_zem.png", lambda: paradit_plaukta_saturu("bigcarp_zem.png", "BigCarp Zemene 1kg", "4.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 215, 75, "sekrbreksis.png", lambda: paradit_plaukta_saturu("sekrbreksis.png", "Sekr Breksis Melns 1kg", "3.90"))

izveidot_attelu_pogu(tirdzniecibas_skats, 280, 75, "sekrlinkar.png", lambda: paradit_plaukta_saturu("sekrlinkar.png", "Sekr LīnKar Marc 1kg", "3.90"))

izveidot_attelu_pogu(tirdzniecibas_skats, 85, 134, "speclinkar.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 11.", "speclinkar.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 150, 134, "specuni.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 13.", "specuni.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 215, 134, "specfeeder.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 15.", "specfeeder.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 280, 134, "specbrek.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 17.", "specbrek.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 75, 205, "universala750.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 22.", "universala750.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 129, 205, "karpa750.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 23.", "karpa750.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 183, 205, "feeder750.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 24.", "feeder750.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 235, 205,  "linkar750.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 25.", "linkar750.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 290, 205, "breksis750.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 26.", "breksis750.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 73, 266, "waftersource.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 31.", "waftersource.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 119, 266, "waftertignut.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 32.", "waftertignut.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 163, 266, "naktstarpi.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 33.", "naktstarpi.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 210, 266, "graudumix.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 34.", "graudumix.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 251, 266, "fluomix.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 35.", "fluomix.png"))

izveidot_attelu_pogu(tirdzniecibas_skats, 294, 266, "fluozala.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 36.", "fluozala.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 72, 326, "kukuruza.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 41.", "kukuruza.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 103, 326, "melase.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 42.", "melase.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 132, 326, "nr4.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 43.", "nr4.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 161, 326, "nr4.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 44.", "nr4.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 190, 326, "nr4.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 45.", "nr4.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 220, 326, "nr3.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 46.", "nr3.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 247, 326, "nr3.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 47.", "nr3.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 278, 326, "nr3.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 48.", "nr3.png"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 309, 326, "nr3.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 49.", "nr3.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 72, 375, "baltie.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 51.", "baltie.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 103, 375, "baltie.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 52.", "baltie.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 132, 375, "baltie.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 53.", "baltie.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 161, 375, "baltie.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 54.", "baltie.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 190, 375, "baltie.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 55.", "baltie.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 220, 375, "pinki.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 56.", "pinki.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 247, 375, "nr2.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 56.", "nr2.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 278, 375, "nr2.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 57.", "nr2.png"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 309, 375, "nr2.png", lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 58.", "nr2.png"))

lokacijas_poga = tk.Button(tirdzniecibas_skats, text="FISHING24-7 tirdzniecības automātu lokācijas", font=("Verdana", 14), fg="#b90843", bg="white", borderwidth=0, command=lokacijas_poga)
lokacijas_poga.pack(pady=(30), anchor="e", padx=100) 

instrukcijas_poga = tk.Button(tirdzniecibas_skats, text="Lietošanas instrukcija", font=("Verdana", 14), fg="#b90843", bg="white", borderwidth=0, command=instrukcijas_poga)
instrukcijas_poga.pack(pady=(30), anchor="e", padx=335) 

norekinasanas_poga = tk.Button(tirdzniecibas_skats, text="Iespējamie norēķināšanās veidi", font=("Verdana", 14), fg="#b90843", bg="white", borderwidth=0, command=norekinasanas_poga)
norekinasanas_poga.pack(pady=(30), anchor="e", padx=240) 

lokacijas_skats = tk.Frame(window, bg="#c0d099")

lokacijas_virsraksts = tk.Label(lokacijas_skats, text="FISHING24-7 tirdzniecības automātu lokācijas", font=("Verdana", 18, "bold"), fg="#b90843", bg="#c0d099")
lokacijas_virsraksts.grid(row=0, column=0, columnspan=2, pady=10)

lokacijas_teksts1 = tk.Label(lokacijas_skats, text="1. Siguldā, Strēlnieku ielā 2 - T/C Šokolāde ēkas ziemeļu pusē, pie B ieejas", 
font=("Verdana", 12, "bold"), 
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
font=("Verdana", 12, "bold"), 
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
font=("Verdana", 12, "bold"), 
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
font=("Verdana", 12, "bold"), 
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
font=("Verdana", 12, "bold"), 
fg="black", 
bg="#c0d099", 
wraplength=500, justify="left", anchor="w")
lokacijas_teksts5.grid(row=3, column=1, padx=30, pady=10, sticky="w")

image_path5 = "kalnciema.png" 
image5 = Image.open(image_path5).resize((400, 135))  
photo5 = ImageTk.PhotoImage(image5)
lokacijas_attels5 = tk.Label(lokacijas_skats, image=photo5, bg="#c0d099")
lokacijas_attels5.grid(row=4, column=1, padx=30, pady=1, sticky="w")

atpakal_poga = tk.Button(lokacijas_skats, text="Atpakaļ", font=("Verdana", 14), fg="#b90843", bg="white",  borderwidth=0, command=atpakal)
atpakal_poga.grid(row=6, column=1, sticky="se")

window.mainloop()
