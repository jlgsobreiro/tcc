from models.Account import Account
from repository.usuario import RepositorioAccount
from views.base_crud import SimpleCRUD


class AccountView(SimpleCRUD):
    class Meta:
        meta = Account
        repo = RepositorioAccount

    title = 'Usuarios'



