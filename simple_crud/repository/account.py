from simple_crud.repository.base_mongo import BaseMongo
from simple_crud.models.Account import Account


class RepositorioAccount(BaseMongo):
    class Meta:
        model = Account
