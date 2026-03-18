# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality = item.quality + 1

    def update_backstage_passes(self,item):
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in > 5:
            item.quality += 2
        elif item.sell_in > 0:
            item.quality += 3
        else:
            item.quality = 0

        if item.quality > 50:
            item.quality = 50

        item.sell_in -= 1

    def update_normal_item(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
                continue
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
                continue
            elif item.name == "Sulfuras, Hand of Ragnaros":
                continue
            else:
                self.update_normal_item(item)

