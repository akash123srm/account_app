import django_tables2 as tables
from .models import UserProfile

class UserProfileTable(tables.Table):

    first_name = tables.Column(verbose_name = 'First Name',attrs={"td": {"width": "1.0 cm"}})
    last_name = tables.Column(verbose_name = 'Last Name', attrs={"td": {"width": "1.0 cm"}})
    iban = tables.Column(verbose_name = 'IBAN', attrs={"td": {"width": "1.0 cm"}})
    '''update = tables.TemplateColumn(' <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#update_user_profile_{{ record.pk }}"> Update </button> {% include "partials/modal_update.html" with record=record%}',
                                 verbose_name = 'Update Profile', attrs={"td": {"width": "1.0cm", "align": "center"}})
    delete = tables.TemplateColumn(' <button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#myModalDelete_{{ record.pk }}"> Delete </button> {% include "partials/modal_delete.html" with record=record%}',
                                  verbose_name = 'Delete Profile', attrs={"td": {"width": "1.0cm", "align": "center"}})'''

    class Meta:
        model = UserProfile
        orderable = False
        attrs = {'class': 'table table-striped  table-bordered table-hover table-condensed paleblue'}
        sequence = ['first_name', 'last_name', 'iban']
        fields = ['first_name', 'last_name', 'iban']
