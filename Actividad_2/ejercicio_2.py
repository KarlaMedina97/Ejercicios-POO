from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    UNIDAD_ASTRONOMICA_KM = 149.597870
    LIMITE_CINTURON_ASTEROIDES_UA = 3.4

    def __init__(
        self,
        nombre=None,
        cantidad_satelites=0,
        masa=0.0,
        volumen=0.0,
        diametro=0,
        distancia_media_al_sol=0,
        tipo_planeta=TipoPlaneta.TERRESTRE,
        observable=False,
    ):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_media_al_sol = distancia_media_al_sol
        self.tipo_planeta = tipo_planeta
        self.observable = observable

    def mostrar_atributos(self):
        nombre = self.nombre if self.nombre is not None else "null"
        print(f"Nombre: {nombre}")
        print(f"Cantidad de satelites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km^3")
        print(f"Diametro: {self.diametro} km")
        print(
            "Distancia media al Sol: "
            f"{self.distancia_media_al_sol} millones de km"
        )
        print(f"Tipo de planeta: {self.tipo_planeta.value}")
        print(f"Observable a simple vista: {self.observable}")

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        limite_exterior = (
            self.LIMITE_CINTURON_ASTEROIDES_UA * self.UNIDAD_ASTRONOMICA_KM
        )
        return self.distancia_media_al_sol > limite_exterior


def main():
    tierra = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.972e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_media_al_sol=149.597870,
        tipo_planeta=TipoPlaneta.TERRESTRE,
        observable=True,
    )
    jupiter = Planeta(
        nombre="Jupiter",
        cantidad_satelites=95,
        masa=1.898e27,
        volumen=1.43128e15,
        diametro=139820,
        distancia_media_al_sol=778.5,
        tipo_planeta=TipoPlaneta.GASEOSO,
        observable=True,
    )

    for planeta in (tierra, jupiter):
        planeta.mostrar_atributos()
        print(f"Densidad: {planeta.calcular_densidad()} kg/km^3")
        print(f"Planeta exterior: {planeta.es_planeta_exterior()}")
        print()


if __name__ == "__main__":
    main()
