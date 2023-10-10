import random
import time
import tkinter as tk
from tkinter import messagebox

class generadorNum:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenamientos")
        self.veces = 0
        self.eventos = []
        self.tiempoTranscurrido = 0
        self.diezmil = False

        # Crear una instancia de Listbox
        self.eventos_listbox = None  # Inicialmente, no se crea la lista

    def main_menu(self):
        # Etiquetas
        Menu_label = tk.Label(root, text="Menú de práctica 2, selecciona una opción: ", font=("Helvetica", 15))
        Menu_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        Menu_Cantidad = tk.Label(root, text="Haz tocado el boton de generar: ", font=("Helvetica", 8))
        Menu_Cantidad.place(relx=0.8, rely=0.30, anchor=tk.CENTER)

        Menu_CantidadTotal = tk.Label(root, text="Total de elementos:", font=("Helvetica", 8))
        Menu_CantidadTotal.place(relx=0.85, rely=0.35, anchor=tk.CENTER)

        # Botón para agregar evento
        boton1 = tk.Button(root, text="Generar 10 números aleatorios", command=self.menu_anadir_num, font=("Helvetica", 15))
        boton1.place(relx=.5, rely=0.5, anchor=tk.CENTER)

        # Botón para agregar evento
        botonDelosDiezmil = tk.Button(root, text="Generar 100,000", command=self.agregar_cienmil, height=2, font=("Helvetica", 9))
        botonDelosDiezmil.place(relx=.15, rely=0.5, anchor=tk.CENTER)


        # Tercer botón
        boton3 = tk.Button(root, text="Ordenar", command=self.numerosOrdenados, width=20, font=("Helvetica", 15))
        boton3.place(relx=.5, rely=0.6, anchor=tk.CENTER)

        TiempoT = tk.Label(root, text="Tiempo en ordenar", font=("Helvetica", 8))
        TiempoT.place(relx=.8, rely=0.56, anchor=tk.CENTER)

        # Cuarto botón para buscar
        boton4 = tk.Button(root, text="Buscar", command=self.buscar_numero, width=20, font=("Helvetica", 15))
        boton4.place(relx=.5, rely=0.7, anchor=tk.CENTER)

        # Cuadro de texto para la búsqueda
        self.buscar_entry = tk.Entry(root, width=30, font=("Helvetica", 15))
        self.buscar_entry.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.menu_mostrar()


    def agregar_cienmil(self):
        self.diezmil = True
        self.menu_anadir_num()
    def numerosOrdenados(self):
        # Comenzar el contador de tiempo
        inicio = time.time()

        self.eventos = [int(evento) for evento in self.eventos]  # Convertir a enteros
        self.eventos = self.merge_sort(self.eventos)  # Aplicar el ordenamiento
        self.actualizar_listbox()

        # Detener el contador de tiempo
        fin = time.time()

        tiempo = fin - inicio

        self.tiempoTranscurrido = tiempo

        tiempoLabel = tk.Label(root, text="", font=("Helvetica", 13))
        tiempoLabel.place(relx=.85, rely=0.6, anchor=tk.CENTER)
        tiempoLabel.config(text=str(self.tiempoTranscurrido))

    def buscar_numero(self):
        buscar_valor = self.buscar_entry.get()
        if buscar_valor:
            buscar_valor = int(buscar_valor)
            self.eventos = [int(evento) for evento in self.eventos]
            self.eventos = self.merge_sort(self.eventos)
            resultado, iteraciones = self.binary_search(self.eventos, buscar_valor)
            if resultado != -1:
                messagebox.showinfo("Resultado de búsqueda",
                                    f"{buscar_valor} encontrado en la lista")
            else:
                messagebox.showinfo("Resultado de búsqueda", f"{buscar_valor} no encontrado en la lista.")
        else:
            messagebox.showinfo("Error", "Inserta un número válido")

    def binary_search(self, arr, target):
        iterations = 0
        left, right = 0, len(arr) - 1

        while left <= right:
            iterations += 1
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid, iterations
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1, iterations

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        # Dividir la lista en dos mitades
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        # Ordenar las mitades de manera recursiva
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        # Combinar las mitades ordenadas
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    def menu_anadir_num(self):
        if(self.diezmil):
            # Algoritmo para generar 100,000 nuevos números aleatorios
            for _ in range(100000):
                nuevos_numeros = random.randint(0, 100000)
                self.eventos.append(nuevos_numeros)
            self.actualizar_listbox()
            self.veces += 100000
            self.diezmil = False
        else:
            # Algoritmo para generar 10 nuevos números aleatorios
            for _ in range(10):
                nuevos_numeros = random.randint(0, 100000)
                self.eventos.append(nuevos_numeros)
            self.actualizar_listbox()
            self.veces += 1

        # Etiqueta para mostrar el número de veces presionado
        label_numero = tk.Label(root, text="", font=("Helvetica", 8))
        label_numero.place(relx=0.95, rely=0.30, anchor=tk.CENTER)
        label_numero.config(text=str(self.veces))
        label_numero2 = tk.Label(root, text="", font=("Helvetica", 8))
        label_numero2.place(relx=0.95, rely=0.35, anchor=tk.CENTER)
        label_numero2.config(text=str(self.veces * 10))

    def menu_mostrar(self):
        # Crea un nuevo Listbox si no existe
        self.eventos_listbox = tk.Listbox(root, width=99)
        self.eventos_listbox.grid(row=0, column=0, columnspan=2)

        self.actualizar_listbox()

    def agregar_usuario(self, nombre):
        if nombre:
            evento = str(nombre)
            self.eventos.append(evento)

    def actualizar_listbox(self):
        if self.eventos_listbox:
            self.eventos_listbox.delete(0, tk.END)
            for evento in self.eventos:
                self.eventos_listbox.insert(tk.END, evento)

if __name__ == "__main__":
    root = tk.Tk()  # inicializa el objeto tk
    root.geometry("600x600")  # cambia el tamaño de la ventana
    app = generadorNum(root)
    app.main_menu()
    root.mainloop()