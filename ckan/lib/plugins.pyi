from ckan.model.user import User
from ckan.model.package import Package
from typing import Any, Dict, List, Optional

def reset_package_plugins() -> None: ...
def reset_group_plugins() -> None: ...
def lookup_package_plugin(package_type: Optional[str] = ...) -> Any: ...
def lookup_group_plugin(group_type: Optional[str] = ...) -> Any: ...
def lookup_group_controller(
    group_type: Optional[str] = ...,
) -> Optional[str]: ...
def lookup_group_blueprints(
    group_type: Optional[str] = ...,
) -> Optional[str]: ...
def register_package_plugins() -> None: ...
def register_package_blueprints(app: Any) -> None: ...
def set_default_package_plugin() -> None: ...
def register_group_plugins() -> None: ...
def register_group_blueprints(app: Any) -> None: ...
def set_default_group_plugin() -> None: ...
def get_permission_labels() -> Any: ...

class DefaultDatasetForm(object):
    def create_package_schema(self) -> Dict: ...
    def update_package_schema(self) -> Dict: ...
    def show_package_schema(self) -> Dict: ...
    def setup_template_variables(
        self, context: Dict, data_dict: Dict
    ) -> None: ...
    def new_template(self) -> str: ...
    def read_template(self) -> str: ...
    def edit_template(self) -> str: ...
    def search_template(self) -> str: ...
    def history_template(self) -> None: ...
    def resource_template(self) -> str: ...
    def package_form(self) -> str: ...
    def resource_form(self) -> str: ...

class DefaultGroupForm(object):
    def group_controller(self) -> str: ...
    def new_template(self) -> str: ...
    def index_template(self) -> str: ...
    def read_template(self) -> str: ...
    def about_template(self) -> str: ...
    def edit_template(self) -> str: ...
    def activity_template(self) -> str: ...
    def admins_template(self) -> str: ...
    def bulk_process_template(self) -> str: ...
    def group_form(self) -> str: ...
    def form_to_db_schema_options(self, options: Dict) -> Dict: ...
    def form_to_db_schema_api_create(self) -> Dict: ...
    def form_to_db_schema_api_update(self) -> Dict: ...
    def form_to_db_schema(self) -> Dict: ...
    def db_to_form_schema(self) -> Dict: ...
    def db_to_form_schema_options(self, options: Dict) -> Dict: ...
    def check_data_dict(self, data_dict: Dict) -> Dict: ...
    def setup_template_variables(
        self, context: Dict, data_dict: Dict
    ) -> None: ...

class DefaultOrganizationForm(DefaultGroupForm):
    def group_controller(self) -> str: ...
    def group_form(self) -> str: ...
    def setup_template_variables(
        self, context: Dict, data_dict: Dict
    ) -> None: ...
    def new_template(self) -> str: ...
    def about_template(self) -> str: ...
    def index_template(self) -> str: ...
    def admins_template(self) -> str: ...
    def bulk_process_template(self) -> str: ...
    def read_template(self) -> str: ...
    def edit_template(self) -> str: ...
    def activity_template(self) -> str: ...

class DefaultTranslation(object):
    def i18n_directory(self) -> str: ...
    def i18n_locales(self) -> List[str]: ...
    def i18n_domain(self) -> str: ...

class DefaultPermissionLabels(object):
    def get_dataset_labels(self, dataset_obj: Package) -> List[str]: ...
    def get_user_dataset_labels(self, user_obj: User) -> List[str]: ...