#? engine
from dataclasses import dataclass, field

from psutil import users
# from config.env import SUPER_ADMIN_ID
from libs.bot_engine.users.User import User, NewUser

from libs.bot_engine.enums.User import AccessLevel


#! 1. Теперь здесь можно создавать переменные ячейки, например
#! передавать объект с ключами (лучше Enum) для создания каталогов Cache
# catalogs = [Cache.USERS, Cache.VERSIONS] и т.д

#! 2. Вернуть выпиленные initial users :( (не горит)

@dataclass
class Cache:
    SUPER_ADMIN_ID: int
    _users: list[User] = field(init=False)  

    def __post_init__(self):
        #? clean start - no users in cache
        self._users = []

            
    def cache_user(self, user: User) -> None:
        is_user_in_cache = self.check_if_user_exists(user.user_id)

        if is_user_in_cache:
            return
        else: 
            self._users.append(user)
        
        
    def get_users_from_cache(self) -> list:
        if len(self._users) > 0:
            # print(f"🟢 users in cache: { self.cached_users }")
            return self._users
        else:
            # print(f"❌ no users in cache: { self.cached_users }")
            return []
    
    
    def get_admin_ids(self) -> list:
        # print(f"admin ids: { self.admin_ids }")
        return self.admin_ids
    
    
    def find_active_user(self, user_id: int) -> User | None:
        # print(f"user_id (Cache.find_active_user): { user_id }")
        for user in self._users:
            # print(f"user: { user }")
            if user.user_id == user_id:
                return user
        # if user not found
        return None
    

    def update_user(self, user_id: int, key: str, new_value: str | int | bool):
        """ updates user in cache"""
        print(f"Updating user with id {user_id} in cache..")

        for user in self._users:
            if user.user_id == user_id:
                # Handle enum conversion if needed
                if key == "access_level" and isinstance(new_value, str):
                    new_value = AccessLevel(new_value)

                setattr(user, key, new_value)

                print(f"🍏 Update user: {user_id} updated with '{key}'='{new_value}'")
                break
                

    def get_user(self, user_id: int) -> dict:
        for user in self._users:
            if user.user_id == user_id:
                return user
            
            
    def remove_user(self, user_id: int) -> None:
        for cache_user in self._users:
            if user_id == cache_user.user_id:
                self._users.remove(cache_user)
                print(f"User removed from cache!")
                
    
    def check_if_user_exists(self, user_id: int) -> bool:
        for user in self._users:
            if user.user_id == user_id:
                print(f"🟡 user exists in Cache: {user_id}")
                return True
            else:
                print(f"🔴 user doesn't exists in Cache: {user_id}")
                return False
        

    
    def find_user_by_property(self, property_name, value):
        for user in self._users:
            if property_name in user:
                if value == user[property_name]:
                    print("🐍 user (find_user_by_property): ",user)
                    return user
                

    def clean_users(self):
        """ cleans all users, except super_admin """
        self._users = []
        
        # for user in self.users:
        #     if user.user_id == self.SUPER_ADMIN_ID:
        #         pass
        #     else:
        #         self.users.remove(user)
        
        print(f"Кеш пользователей очищен! 🧹\n{self._users}")
