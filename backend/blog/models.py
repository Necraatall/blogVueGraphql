import random
from typing import List
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    website = models.URLField(blank=True, null=True)
    bio = models.CharField(max_length=240, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})


# cizi klice:
# b = Book.objects.get(id=50)

"""    
class Student(models.Model):
    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshman")
        SOPHOMORE = "SO", _("Sophomore")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }

    def get_year_in_school(self) -> YearInSchool:
        # Get value from choices enum
        return self.YearInSchool[self.year_in_school]




According to the Django docs, something along the lines of the following should do:

class House(models.Model):
    Floor = models.IntegerChoices('Floor', range(1,11))
    floors = IntegerField(choices=Floor.choices)
"""
META_RACE = random.choice(["Human", "Ork", "Dwarven", "Elven", "Troll"])
magic_value: int
resonance_value: int
loop_result: int


def choce_atribute_style():
    # TODO if selectbox is on BS numbers [100, 150, 200, 250, 300, 345] - see on previous project
    return [4, 4, 2, 2, 2, 2, 1, 1]


chosen_atribute_values: List[int] = choce_atribute_style()


def race_cost_bs():
    if META_RACE == "Ork":
        return 20
    if META_RACE == "Dwarven":
        return 25
    if META_RACE == "Elven":
        return 30
    if META_RACE == "Troll":
        return 40


def race_meta_ability():
    if META_RACE == "Ork":
        return "Low-Light Vision"
    if META_RACE == "Dwarven":
        return "Thermographic Vision, +2 dice for Body Tests to resist pathogens and toxins"
    if META_RACE == "Elven":
        return "Low-Light Vision"
    if META_RACE == "Troll":
        return "Thermographic Vision, +1 Reach, +1 natural armor (cumulative with worn armor)"


def metahuman_race_bonuses():
    if META_RACE == "Human":
        lis_of_bonuses = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    if META_RACE == "Ork":
        lis_of_bonuses = [3, 0, 0, 2, -1, 0, -1, 0, 0]
    if META_RACE == "Dwarven":
        lis_of_bonuses = [1, 0, -1, 2, 0, 0, 0, 0, 0]
    if META_RACE == "Elven":
        lis_of_bonuses = [0, 1, 0, 0, 2, 0, 0, 0, 0]
    if META_RACE == "Troll":
        lis_of_bonuses = [4, -1, 0, 4, -2, -1, -1, 0, 0]
    return lis_of_bonuses


def decide_magic():
    magic_decide = random.randint(1, 100)
    if magic_decide >= 95:
        return random.choice(["resonance", "shaman", "mage", "adept", "physical_adept"])
    else:
        return "without magic"


def get_value_for_atr():
    for numbval in chosen_atribute_values:
        loop_result = numbval
    return loop_result


def get_bonus_for_atr():
    for numbval in metahuman_race_bonuses():
        loop_result = numbval
    return loop_result


def get_value_for_edge():
    # TODO: if human +1
    return random.randint(1, 6)


def kit_bonuses():
    # TODO after Merits and Flaws, skills and magic will be done
    return 0


def get_ware_cost():
    # TODO for now its 6 default, after implementing others, will be inherited from another "nested" tables
    return 6


def get_negative_essence():
    # TODO after ware illnesses and their types of implamentations
    return 0


def get_more_initiative_phases():
    # TODO after magic and cyberware
    return 0


# author = models.ForeignKey(Profile, on_delete=models.PROTECT)


class Atributes(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    race_cost = models.IntegerField(default=race_cost_bs())
    meta_race = models.CharField(META_RACE)
    meta_ability = models.CharField(race_meta_ability())
    body = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    agility = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    reaction = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    strength = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    charisma = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    intuition = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    logic = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    willpower = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    edge = models.IntegerField(
        default=get_value_for_atr() + get_bonus_for_atr() + kit_bonuses()
    )
    essence = models.IntegerField(default=get_ware_cost + get_negative_essence())
    magic = models.IntegerField(
        default=get_value_for_atr() - get_ware_cost() - get_negative_essence()
    )
    resonance = models.IntegerField(
        default=get_value_for_atr() - get_ware_cost() - get_negative_essence()
    )
    initiative = models.IntegerField()
    initiative_astral = models.IntegerField()
    initiative_phases = models.IntegerField(1 + get_more_initiative_phases())
    initiative_astral_phases = models.IntegerField()
    physical_damage_track = models.IntegerField()
    stun_damage_track = models.IntegerField()
