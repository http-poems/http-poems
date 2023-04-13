from django.db import models, transaction
from django.db.models import Count, Max, Min

from apps.poems.exceptions import SmallPopulationSize
from apps.poems.utils import min_max, min_max_count


class RandomQuerySet(models.query.QuerySet):
    def random(self, amount=1):
        with transaction.atomic():
            aggregates = self.aggregate(
                min_id=Min("id"), max_id=Max("id"), count=Count("id")
            )

            if not aggregates["count"]:
                return self.none()

            if aggregates["count"] <= amount:
                return self.all()

            if (aggregates["max_id"] - aggregates["min_id"]) + 1 == aggregates["count"]:
                return self.filter(
                    id__in=min_max(
                        amount,
                        aggregates["min_id"],
                        aggregates["max_id"],
                        aggregates["count"],
                    )
                )

            try:
                selected_ids = min_max_count(
                    amount,
                    aggregates["min_id"],
                    aggregates["max_id"],
                    aggregates["count"],
                )
            except SmallPopulationSize:
                selected_ids = self.values_list("id", flat=True)

            assert len(selected_ids) > amount
            return self.filter(id__in=selected_ids).order_by("?")[:amount]
