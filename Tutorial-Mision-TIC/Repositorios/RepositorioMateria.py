from bson import ObjectId
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Materia import Materia
class RepositorioMateria(InterfaceRepositorio[Materia]):
    def getListadoMateriasEnDepartamento(self, id_materia):
        theQuery = {"departamento.$id": ObjectId(id_materia)}
        return self.query(theQuery)