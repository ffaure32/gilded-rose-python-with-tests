SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
MAX_HYPE = 5
MEDIUM_HYPE = 10
MAX_QUALITY = 50


class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update(self):
        self.decrease_quality()
        self.decrease_sell_in()
        if self.deprecated():
            self.decrease_quality()

    def decrease_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def increase_quality_to_max(self):
        if self.quality < MAX_QUALITY:
            self.increase_quality()

    def increase_quality(self):
        self.quality += 1

    def decrease_sell_in(self):
        self.sell_in -= 1

    def deprecated(self):
        return self.sell_in < 0

class VintageItem(Item):
    def update(self):
        self.update_vintage_quality()
        self.decrease_sell_in()
        if self.deprecated():
            self.reset_quality()

    def update_vintage_quality(self):
        self.increase_quality_to_max()
        if self.sell_in <= MAX_HYPE:
            self.increase_quality_to_max()
        if self.sell_in <= MEDIUM_HYPE:
            self.increase_quality_to_max()

    def reset_quality(self):
        self.quality = 0

class LegendaryItem(Item):
    def update(self):
        pass
