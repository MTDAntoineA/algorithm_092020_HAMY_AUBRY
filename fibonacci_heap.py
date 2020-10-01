
class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass



class FibonacciHeap(Heap):
    

        def __init__(self):

            self.arbre1 = [2,5,8]
            self.arbre2 = [4,10,12]
            self.size = 0

        def insert(self, value: int) -> None:
            
            self.arbre1.append(value)
            self.size += 1

            print(self.arbre1)

            pass

        def find_min(self, value) -> int:

            varMin = min(self.arbre1)

            if varMin > value:
                    varMin = value
                    print(varMin)
            else:
                    print(varMin)
                    pass 

        def delete_min(self, value) -> int:

            """
            self.pop(value)
            Supprime et retourne la valeur minimum dans l'arbre
            """
            pass

        def merge(self, fibonnaci_heap: Heap) -> None:
            
            """
            Fusionne deux arbres
            """
            self.arbre1.extend(self.arbre2)
            print(self.arbre1)

            """
            Afficher la nouvelle valeur min
            """
            varMin = min(self.arbre1)
            varMin2 = min(self.arbre2)

            if varMin > varMin2:
                varMin = varMin2
                print(varMin)
            else:
                print(varMin)
                pass


heap = FibonacciHeap()
heap.insert(18)
heap.find_min(90)
heap.merge(heap)