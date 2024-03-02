from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.collections.models import Payment


@receiver(post_save, sender=Payment)
def reset_cache_collected_amount(
    sender, instance=None, created=False, **kwargs
):
    """
    Сигнал сбрасывающий закэшированное значение collected_amount для
    денежного сбора.
    """

    collect_id = instance.collect_id

    collected_amount_cache_key = f"collect_collected_amount_{collect_id}"
    cache.delete(collected_amount_cache_key)


@receiver(post_save, sender=Payment)
def reset_cache_contributors_count(
    sender, instance=None, created=False, **kwargs
):
    """
    Сигнал сбрасывающий закэшированное значение contributors_count для
    денежного сбора.
    """

    collect_id = instance.collect_id

    contributors_count_cache_key = f"collect_contributors_count_{collect_id}"
    cache.delete(contributors_count_cache_key)
