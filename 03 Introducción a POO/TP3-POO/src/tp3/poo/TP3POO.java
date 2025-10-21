/* 
 * Para una correcta ejecución del código, separar bloques por puntos de TP3.
 * En animos de facilitar la entrega y recepción del mismo, el TP fue realizado bajo un mismo archivo conteniendo consignas y resolución.
 * Realizado por Reynoso Arellano, Franco Gastón. 
 */
package tp3.poo;

/* 
 * 1) Crear una clase Estudiante con los atributos: nombre, apellido, curso, calificación
*/
public class Estudiante {
    String nombre;
    String apellido;
    String curso;
    double calificacion; // 0..10

    public Estudiante(String nombre, String apellido, String curso, double calificacion) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.curso = curso;
        this.calificacion = calificacion;
    }

    public void mostrarInfo() {
        System.out.printf("Estudiante: %s %s | Curso: %s | Calificación: %.1f%n",
                nombre, apellido, curso, calificacion);
    }

    public void subirCalificacion(double puntos) {
        calificacion = Math.min(10.0, calificacion + puntos);
    }

    public void bajarCalificacion(double puntos) {
        calificacion = Math.max(0.0, calificacion - puntos);
    }
}

/* 
 * 2) Crear una clase Mascota con los atributos: nombre, especie, edad.
*/

public class Mascota {
    String nombre;
    String especie;
    int edad;

    public Mascota(String nombre, String especie, int edad) {
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public void mostrarInfo() {
        System.out.printf("Mascota: %s | Especie: %s | Edad: %d%n",
                nombre, especie, edad);
    }

    public void cumplirAnios() {
        edad++;
    }
}

/* 
 * 3) Crear una clase Libro con atributos privados: titulo, autor, añoPublicacion
*/

import java.time.Year;
public class Libro {
    // Encapsulados
    private String titulo;
    private String autor;
    private int anioPublicacion;

    public Libro(String titulo, String autor, int anioPublicacion) {
        this.titulo = titulo;
        this.autor = autor;
        setAnioPublicacion(anioPublicacion); // usa la validación
    }

    // Getters
    public String getTitulo() { return titulo; }
    public String getAutor() { return autor; }
    public int getAnioPublicacion() { return anioPublicacion; }

    // Setter con validación
    public void setAnioPublicacion(int anio) {
        int anioActual = Year.now().getValue();
        // margen básico de validez: desde la imprenta de Gutenberg (~1450)
        if (anio >= 1450 && anio <= anioActual) {
            this.anioPublicacion = anio;
        } else {
            System.out.println("Año inválido: " + anio + " (se mantiene el anterior: " + this.anioPublicacion + ")");
        }
    }

    public void mostrarInfo() {
        System.out.printf("Libro: \"%s\" de %s (%d)%n", titulo, autor, anioPublicacion);
    }
}
