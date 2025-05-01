class InformacionComun:
    def __init__(self, fecha_caducidad, no_lote):
        self.__fecha_caducidad = fecha_caducidad
        self.__no_lote = no_lote


    def get_fecha_caducidad(self):
        return self.__fecha_caducidad

    def set_fecha_caducidad(self, fecha_caducidad):
        self.__fecha_caducidad = fecha_caducidad

    def get_no_lote(self):
        return self.__no_lote

    def set_no_lote(self, nuevo_lote):
        self.__no_lote = nuevo_lote
    
    def mostrar_info(self):
        print("Fecha de caducidad:", self.__fecha_caducidad)
        print("Numero de lote:", self.__no_lote)

class EnvasadoYPais(InformacionComun):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen):
        super().__init__(fecha_caducidad, no_lote)
        self.__fecha_envasado = fecha_envasado
        self.__pais_de_origen = pais_de_origen

    def get_fecha_envasado(self):
        return self.__fecha_envasado
    
    def set_fecha_envasado(self, fecha_envasado):
        self.__fecha_envasado = fecha_envasado

    def get_pais_de_origen(self):
        return self.__pais_de_origen
    
    def set_pais_de_origen(self, pais_de_origen):
        self.__pais_de_origen = pais_de_origen

    def mostrar_info(self):
        super().mostrar_info()
        print("Fecha de envasado:", self.__fecha_envasado)
        print("Pais de origen:", self.__pais_de_origen)


class ProductoFresco(EnvasadoYPais):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen):
        super().__init__(fecha_caducidad, no_lote, fecha_envasado, pais_de_origen)

class TemperaturaRecomendada(EnvasadoYPais):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada):
        super().__init__(fecha_caducidad, no_lote, fecha_envasado, pais_de_origen)
        self.__temperatura_de_mantenimiento_recomendada = temperatura_de_mantenimiento_recomendada
    
    def get_temperatura_de_mantenimiento_recomendada(self):
        return self.__temperatura_de_mantenimiento_recomendada
    
    def set_temperatura_de_mantenimiento_recomendada(self, temperatura_de_mantenimiento_recomendada):
        self.__temperatura_de_mantenimiento_recomendada = temperatura_de_mantenimiento_recomendada

    def mostrar_info(self):
        super().mostrar_info()
        print("Temperatura de mantenimiento recomendada:", self.__temperatura_de_mantenimiento_recomendada)

class ProductoRefrigerado(TemperaturaRecomendada):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada, codigo_del_organismo_de_supervision_alimentaria):
        super().__init__(fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada)
        self.__codigo_del_organismo_de_supervision_alimentaria = codigo_del_organismo_de_supervision_alimentaria

    def get_codigo_del_organismo_de_supervision_alimentaria(self):
        return self.__codigo_del_organismo_de_supervision_alimentaria
    
    def set_codigo_del_organismo_de_supervision_alimentaria(self, codigo_del_organismo_de_supervision_alimentaria):
        self.__codigo_del_organismo_de_supervision_alimentaria = codigo_del_organismo_de_supervision_alimentaria

    def mostrar_info(self):
        super().mostrar_info()
        print("Codigo del organismo de supervision alimentaria:", self.__codigo_del_organismo_de_supervision_alimentaria)

class ProductoCongelado(TemperaturaRecomendada):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada):
        super().__init__(fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada)

class CongeladosAire(ProductoCongelado):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada, porcentaje_nitrogeno, porcentaje_oxigeno, porcentaje_dioxido_carbono, porcentaje_vapor_agua):
        super().__init__(fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada)
        self.__porcentaje_nitrogeno = porcentaje_nitrogeno
        self.__porcentaje_oxigeno = porcentaje_oxigeno
        self.__porcentaje_dioxido_carbono = porcentaje_dioxido_carbono
        self.__porcentaje_vapor_agua = porcentaje_vapor_agua

    def get_porcentaje_nitrogeno (self):
        return self.__porcentaje_nitrogeno
    
    def set_porcentaje_nitrogeno (self, porcentaje_nitrogeno):
        self.__porcentaje_nitrogeno = porcentaje_nitrogeno

    def get_porcentaje_oxigeno (self):
        return self.__porcentaje_oxigeno
    
    def set_porcentaje_oxigeno (self, porcentaje_oxigeno):
        self.__porcentaje_oxigeno = porcentaje_oxigeno
    
    def get_porcentaje_dioxido_carbono (self):
        return self.__porcentaje_dioxido_carbono
    
    def set_porcentaje_dioxido_carbono (self, porcentaje_dioxido_carbono):
        self.__porcentaje_dioxido_carbono = porcentaje_dioxido_carbono

    def get_porcentaje_vapor_agua (self):
        return self.__porcentaje_vapor_agua
    
    def set_porcentaje_vapor_agua (self, porcentaje_vapor_agua):
        self.__porcentaje_vapor_agua = porcentaje_vapor_agua

    def mostrar_info(self):
        super().mostrar_info()
        print("El porcentaje de nitrogeno es:", self.__porcentaje_nitrogeno)
        print("El porcentaje de oxigeo es:", self.__porcentaje_oxigeno)
        print("El porcentaje de carbono es:", self.__porcentaje_dioxido_carbono)
        print("El porcentaje del vapor del agua es:", self.__porcentaje_vapor_agua)

class CongeladosAgua(ProductoCongelado):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada, informacion_salinidad):
        super().__init__(fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada)
        self.__informacion_salinidad = informacion_salinidad
        
    def get_informacion_salinidad (self):
        return self.__informacion_salinidad
    
    def set_informacion_salinidad (self, informacion_salinidad):
        self.__informacion_salinidad = informacion_salinidad

    def mostrar_info(self):
        super().mostrar_info()
        print("La informacion de la salinidad del agua con que se realizo la congelación en gramos de sal por litro de agua es: ", self.__informacion_salinidad)
 
class CongeladosNitrogeno(ProductoCongelado):
    def __init__(self, fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada, metodo_congelacion, tiempo_exposicion_nitrogeno):
        super().__init__(fecha_caducidad, no_lote, fecha_envasado, pais_de_origen, temperatura_de_mantenimiento_recomendada)
        self.__metodo_congelacion = metodo_congelacion
        self.__tiempo_exposicion_nitrogeno = tiempo_exposicion_nitrogeno

    def get_metodo_congelacion (self):
        return self.__metodo_congelacion
    
    def set_metodo_congelacion (self, metodo_congelacion):
        self.__metodo_congelacion = metodo_congelacion

    def get_tiempo_exposicion_nitrogeno (self):
        return self.__tiempo_exposicion_nitrogeno
    
    def set_tiempo_exposicion_nitrogeno (self, tiempo_exposicion_nitrogeno):
        self.__tiempo_exposicion_nitrogeno = tiempo_exposicion_nitrogeno

    def mostrar_info(self):
        super().mostrar_info()
        print("Metodo de congelacion empleado : ", self.__metodo_congelacion)
        print("Tiempo de exposicion al nitrogeno expresado en segundos: ", self.__tiempo_exposicion_nitrogeno)

class testHerencia3:
    def main(self):
        print("Frescos:")
        fresco1 = ProductoFresco("30/04/25", "LOTE001", "26/04/25", "Mexico")
        fresco2 = ProductoFresco("05/05/25", "LOTE002", "27/04/25", "Espana")
        print("Producto Fresco 1:")
        fresco1.mostrar_info()
        print("Producto Fresco 2:")
        fresco2.mostrar_info()

        print("Refrigerados:")
        refrigerado1 = ProductoRefrigerado("28/04/25", "REF001", "25/04/25", "Canada", "4°C", "OSAL-CA-123")
        refrigerado2 = ProductoRefrigerado("02/05/25", "REF002", "26/04/25", "Argentina", "2°C", "OSAL-AR-456")
        refrigerado3 = ProductoRefrigerado("01/05/25", "REF003", "27/04/25", "Brasil", "3°C", "OSAL-BR-789")
        print("Producto Refrigerado 1:")
        refrigerado1.mostrar_info()
        print("Producto Refrigerado 2:")
        refrigerado2.mostrar_info()

        print("Congelados Agua:")
        congelado_agua1 = CongeladosAgua("30/06/26", "CONG01A", "20/06/26", "Noruega", "-18°C", "30 g/L")
        congelado_agua2 = CongeladosAgua("15/07/26", "CONG02A", "25/06/26", "Chile", "-20°C", "35 g/L")
        print("Producto Congelado Agua 1:")
        congelado_agua1.mostrar_info()
        print("Producto Congelado Agua 2:")
        congelado_agua2.mostrar_info()

        print("Congelados Aire:")
        congelado_aire1 = CongeladosAire("20/05/26", "CONG01AIRE", "10/05/26", "Japon", "-22°C", "78%", "21%", "0.04%", "0.96%")
        congelado_aire2 = CongeladosAire("25/05/26", "CONG02AIRE", "12/05/26", "Corea del Sur", "-25°C", "79%", "20%", "0.03%", "0.97%")
        print("Producto Congelado Aire 1:")
        congelado_aire1.mostrar_info()
        print("Producto Congelado Aire 2:")
        congelado_aire2.mostrar_info()

        print("Congelados Nitrogeno:")
        congelado_nitrogeno1 = CongeladosNitrogeno("10/06/26", "CONG01N2", "01/06/26", "Francia", "-30°C", "Inmersion", "120")
        print("Producto Congelado Nitrogeno:")
        congelado_nitrogeno1.mostrar_info()
  

if __name__ == "__main__":
    test = testHerencia3()
    test.main()