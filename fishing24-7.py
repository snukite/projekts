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

    instrukcijas_attels_path = "bildes/instrukcija.png" 
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

    norekinasanas_attels_path = "bildes/norekinasanas.png" 
    norekinasanas_image = Image.open(norekinasanas_attels_path)
    norekinasanas_photo = ImageTk.PhotoImage(norekinasanas_image)

    attels_label2 = tk.Label(norekinasanas_logs, image=norekinasanas_photo, bg="#c0d099")
    attels_label2.image = norekinasanas_photo  
    attels_label2.pack()

    aizvert_poga = tk.Button(norekinasanas_logs, text="Aizvērt", font=("Verdana", 14), fg="#b90843", bg="white", command=norekinasanas_logs.destroy)
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

original_image = Image.open("bildes/automats.png")
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

tirdzniecibas_attels_path = "bildes/plaukti.png"  
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

izveidot_attelu_pogu(tirdzniecibas_skats, 85, 75, "bildes/bigcarp_kuku.png", lambda: paradit_plaukta_saturu("bildes/bigcarp_kuku.png", "Big Carp Kukurūza", "4.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 150, 75, "bildes/bigcarp_zem.png", lambda: paradit_plaukta_saturu("bildes/bigcarp_zem.png", "BigCarp Zemene 1kg", "4.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 215, 75, "bildes/sekrbreksis.png", lambda: paradit_plaukta_saturu("bildes/sekrbreksis.png", "Sekr Breksis Melns 1kg", "3.90"))

izveidot_attelu_pogu(tirdzniecibas_skats, 280, 75, "bildes/sekrlinkar.png", lambda: paradit_plaukta_saturu("bildes/sekrlinkar.png", "Sekr LīnKar Marc 1kg", "3.90"))

izveidot_attelu_pogu(tirdzniecibas_skats, 85, 134, "bildes/speclinkar.png", lambda: paradit_plaukta_saturu("bildes/speclinkar.png", "Spec LīnisKarūsa 1kg", "3.50"))

izveidot_attelu_pogu(tirdzniecibas_skats, 150, 134, "bildes/specuni.png", lambda: paradit_plaukta_saturu("bildes/specuni.png", "Spec Universālā 1kg", "3.50"))

izveidot_attelu_pogu(tirdzniecibas_skats, 215, 134, "bildes/specfeeder.png", lambda: paradit_plaukta_saturu("bildes/specfeeder.png", "Spec Feeder 1kg", "3.50"))

izveidot_attelu_pogu(tirdzniecibas_skats, 280, 134, "bildes/specbrek.png", lambda: paradit_plaukta_saturu("bildes/specbrek.png", "Spec Breksis 1kg", "3.50"))

izveidot_attelu_pogu(tirdzniecibas_skats, 75, 205, "bildes/universala750.png", lambda: paradit_plaukta_saturu("bildes/universala750.png", "Universālā 750g", "2.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 129, 205, "bildes/karpa750.png", lambda: paradit_plaukta_saturu("bildes/karpa750.png", "Karpa 750g", "2.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 183, 205, "bildes/feeder750.png", lambda: paradit_plaukta_saturu("bildes/feeder750.png", "Feeder 750g", "2.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 235, 205,  "bildes/linkar750.png", lambda: paradit_plaukta_saturu("bildes/linkar750.png", "Līnis-Karūsa 750g", "2.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 290, 205, "bildes/breksis750.png", lambda: paradit_plaukta_saturu("bildes/breksis750.png", "Breksis 750g", "2.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 73, 266, "bildes/waftersource.png", lambda: paradit_plaukta_saturu("bildes/waftersource.png", " Vafteri Source 15mm", "6.00"))

izveidot_attelu_pogu(tirdzniecibas_skats, 119, 266, "bildes/waftertignut.png", lambda: paradit_plaukta_saturu("bildes/waftertignut.png", "Vafteri TigNut 15mm", "7.50"))

izveidot_attelu_pogu(tirdzniecibas_skats, 163, 266, "bildes/naktstarpi.png", lambda: paradit_plaukta_saturu("bildes/naktstarpi.png", "Nakstārpi", "4.50"))

izveidot_attelu_pogu(tirdzniecibas_skats, 210, 266, "bildes/graudumix.png", lambda: paradit_plaukta_saturu("bildes/graudumix.png", "Graudu Mix 500g", "3.50"))

izveidot_attelu_pogu(tirdzniecibas_skats, 251, 266, "bildes/fluomix.png", lambda: paradit_plaukta_saturu("bildes/fluomix.png", "Piedeva FluoMix 400g", "4.90"))

izveidot_attelu_pogu(tirdzniecibas_skats, 294, 266, "bildes/fluozala.png", lambda: paradit_plaukta_saturu("bildes/fluozala.png", "Piedeva FluoZaļ 400g", "5.70"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 72, 326, "bildes/kukuruza.png", lambda: paradit_plaukta_saturu("bildes/kukuruza.png", "Kukurūza 212ml", "4.00"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 103, 326, "bildes/melase.png", lambda: paradit_plaukta_saturu("bildes/melase.png", "Melase Breksis 350g", "2.90"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 132, 326, "bildes/nr4.png", lambda: paradit_plaukta_saturu("bildes/nr4.png", "Sliekas Nr.4", "2.00"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 161, 326, "bildes/nr4.png", lambda: paradit_plaukta_saturu("bildes/nr4.png", "Sliekas Nr.4", "2.00"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 190, 326, "bildes/nr4.png", lambda: paradit_plaukta_saturu("bildes/nr4.png", "Sliekas Nr.4", "2.00"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 220, 326, "bildes/nr3.png", lambda: paradit_plaukta_saturu("bildes/nr3.png", "Sliekas Nr.3", "2.00"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 247, 326, "bildes/nr3.png", lambda: paradit_plaukta_saturu("bildes/nr3.png", "Sliekas Nr.3", "2.00"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 278, 326, "bildes/nr3.png", lambda: paradit_plaukta_saturu("bildes/nr3.png", "Sliekas Nr.3", "2.00"))

izveidot_attelu_pogu2(tirdzniecibas_skats, 309, 326, "bildes/nr3.png", lambda: paradit_plaukta_saturu("bildes/nr3.png", "Sliekas Nr.3", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 72, 375, "bildes/baltie.png", lambda: paradit_plaukta_saturu("bildes/baltie.png", "Baltie tārpi 50g", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 103, 375, "bildes/baltie.png", lambda: paradit_plaukta_saturu("bildes/baltie.png", "Baltie tārpi 50g", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 132, 375, "bildes/baltie.png", lambda: paradit_plaukta_saturu("bildes/baltie.png", "Baltie tārpi 50g", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 161, 375, "bildes/baltie.png", lambda: paradit_plaukta_saturu("bildes/baltie.png", "Baltie tārpi 50g", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 190, 375, "bildes/baltie.png", lambda: paradit_plaukta_saturu("bildes/baltie.png", "Baltie tārpi 50g", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 220, 375, "bildes/pinki.png", lambda: paradit_plaukta_saturu("bildes/pinki.png", "Pinki 50g", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 247, 375, "bildes/nr2.png", lambda: paradit_plaukta_saturu("bildes/nr2.png", "Sliekas Nr.2", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 278, 375, "bildes/nr2.png", lambda: paradit_plaukta_saturu("bildes/nr2.png", "Sliekas Nr.2", "2.00"))

izveidot_attelu_pogu3(tirdzniecibas_skats, 309, 375, "bildes/nr2.png", lambda: paradit_plaukta_saturu("bildes/nr2.png", "Sliekas Nr.2", "2.00"))

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

image_path = "bildes/sigulda.png" 
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

image_path2 = "bildes/brivibas.png" 
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

image_path3 = "bildes/vaidavas.png" 
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

image_path4 = "bildes/latgales.png" 
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

image_path5 = "bildes/kalnciema.png" 
image5 = Image.open(image_path5).resize((400, 135))  
photo5 = ImageTk.PhotoImage(image5)
lokacijas_attels5 = tk.Label(lokacijas_skats, image=photo5, bg="#c0d099")
lokacijas_attels5.grid(row=4, column=1, padx=30, pady=1, sticky="w")

atpakal_poga = tk.Button(lokacijas_skats, text="Atpakaļ", font=("Verdana", 14), fg="#b90843", bg="white",  borderwidth=0, command=atpakal)
atpakal_poga.grid(row=6, column=1, sticky="se")

window.mainloop()
