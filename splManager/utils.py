from .models import Spl
import uuid


def unique_spl_join_code():
    code = uuid.uuid4().hex[:8].upper()
    spl = Spl.objects.filter(join_code__iexact=code)
    while spl.exists():
        code = uuid.uuid4().hex[:8].upper()
        spl = Spl.objects.filter(join_code__iexact=code)

    return code
