# CRUD - create, read(listing,detail), update, delete


class CreateMixin: 
    def _get_or_set_objects(self): 
        try: 
            self.id
            self.objects
        except (NameError, AttributeError): 
            self.objects = []
            self.id = 0 


    def __init__(self) -> None:
        self._get_or_set_objects()

    def post(self, **kwargs): 
        self.id += 1
        obj = dict(id=self.id, **kwargs)
        self.objects.append(obj)
        return {'status': '201 created','masg':obj}
                
class ReadMixin: #по default у mixin нет своего списка с id, он будет у класса который наследуется от mixina 
    def list(self): 
        res = [{'id':obj['id'], 'title': obj[
            'title'
        ]}
        for obj in self.objects]
        return {'status':'200 OK', 'msg ': res}
    
    def detail(self,id,**kwargs): #алгоритм быстрого поиска по id используя срезы
        objects_id = [x['id'] for x in self.objects] #поиск по id внутри словаря 
        left = 0  
        right = len(objects_id) - 1 #получить крайнее число 
        mid = len(objects_id) // 2 #получить середину

        while objects_id[mid] != id and left <= right: 
            if id < objects_id[mid]: 
                right = mid - 1 #срез в меньшую сторону
            else: 
                left = mid + 1 #сруз в большую сторону 

            mid = (left + right) // 2 
            
        if left > right: 
            return {'status': '404 Not found'}
        return  {'status': '200 OK', 'msg': self.objects[mid]}


       


    
    
    


# obj = CreateMixin()
# obj.post(title = "Redmi Note 10", description = 'The best phone!', qty=10, price=250)

