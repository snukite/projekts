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

def paradit_plaukta_saturu(teksts, attels_path):
    
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

    plaukta_teksts = tk.Label(plaukta_frame, text=teksts, font=("Verdana", 14), fg="#b90843", bg="#c0d099", wraplength=600, justify="left")
    plaukta_teksts.pack(side="right")

    atpakal_poga = tk.Button(plaukta_skats, text="Atpakaļ", font=("Verdana", 14), fg="#b90843", bg="white", borderwidth=0, command=lambda: [plaukta_skats.pack_forget(), tirdzniecibas_skats.pack(fill='both', expand=True)])
    atpakal_poga.pack(pady=20)


plaukta_poga1 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843",  borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 1.", "bigcarp_kuku.png"))
plaukta_poga1.place(x=75, y=90)

plaukta_poga3 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843",  borderwidth=0,command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 3.", "bigcarp_zem.png"))
plaukta_poga3.place(x=140, y=90)

plaukta_poga5 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 5.", "sekrbreksis.png"))
plaukta_poga5.place(x=205, y=90)

plaukta_poga7 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 7.", "sekrlinkar.png"))
plaukta_poga7.place(x=272, y=90)

plaukta_poga11 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 11.", "speclinkar.png"))
plaukta_poga11.place(x=75, y=152)

plaukta_poga13 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 13.", "specuni.png"))
plaukta_poga13.place(x=140, y=152)

plaukta_poga15 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 15.", "specfeeder.png"))
plaukta_poga15.place(x=205, y=152)

plaukta_poga17 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 17.", "specbrek.png"))
plaukta_poga17.place(x=272, y=152)

plaukta_poga22 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 22.", "universala750.png"))
plaukta_poga22.place(x=70, y=220)

plaukta_poga23 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 23.", "karpa750.png"))
plaukta_poga23.place(x=124, y=220)

plaukta_poga24 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 24.", "feeder750.png"))
plaukta_poga24.place(x=176, y=220)

plaukta_poga25 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 25.", "linkar750.png"))
plaukta_poga25.place(x=230, y=220)

plaukta_poga26 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 26.", "breksis750.png"))
plaukta_poga26.place(x=284, y=220)

plaukta_poga31 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 31.", "waftersource.png"))
plaukta_poga31.place(x=67, y=285)

plaukta_poga32 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 32.", "waftertignut.png"))
plaukta_poga32.place(x=112, y=285)

plaukta_poga33 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 33.", "naktstarpi.png"))
plaukta_poga33.place(x=157, y=285)

plaukta_poga34 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 34.", "graudumix.png"))
plaukta_poga34.place(x=202, y=285)

plaukta_poga35 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 35.", "fluomix.png"))
plaukta_poga35.place(x=247, y=285)

plaukta_poga36 = tk.Button(tirdzniecibas_skats, text="Poga!!!", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=lambda: paradit_plaukta_saturu("Šeit ir informācija par Plauktu 36.", "fluozala.png"))
plaukta_poga36.place(x=292, y=285)

plaukta_poga41 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga41.place(x=67, y=338)

plaukta_poga42 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga42.place(x=97, y=338)

plaukta_poga43 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga43.place(x=127, y=338)

plaukta_poga44 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga44.place(x=157, y=338)

plaukta_poga45 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga45.place(x=187, y=338)

plaukta_poga46 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga46.place(x=217, y=338)

plaukta_poga47 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga47.place(x=247, y=338)

plaukta_poga48 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga48.place(x=277, y=338)

plaukta_poga49 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga49.place(x=307, y=338)

plaukta_poga51 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga51.place(x=67, y=384)

plaukta_poga52 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga52.place(x=97, y=384)

plaukta_poga53 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga53.place(x=127, y=384)

plaukta_poga54 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga54.place(x=157, y=384)

plaukta_poga55 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga55.place(x=187, y=384)

plaukta_poga56 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga56.place(x=217, y=384)

plaukta_poga57 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga57.place(x=247, y=384)

plaukta_poga58 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga58.place(x=277, y=384)

plaukta_poga59 = tk.Button(tirdzniecibas_skats, text="Poga", font=("Verdana", 7), fg="white", bg="#b90843", borderwidth=0, command=plaukta_pogas)
plaukta_poga59.place(x=307, y=384)

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
