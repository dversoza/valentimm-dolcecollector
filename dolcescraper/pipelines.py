import re
from itemadapter import ItemAdapter

class DolcescraperPipeline:
    def process_item(self, item, spider):
        # Clean up the "name" value
        item['name'] = item['name'].strip()

        # Clean up the "points" value
        item['points'] = item['points'].strip()

        # Clean up the "description" value
        item['description'] = item['description'].strip()
            
        # Clean up the "price" value
        price_string = item['price']
        price_pattern = r'-?\d+(\.\d+)?'
        match = re.search(price_pattern, price_string)
        if match:
            matched_float_str = match.group()
            try:
                item['price'] = float(matched_float_str)
            except ValueError:
                item['price'] = None
        else:
            item['price'] = None


        return item
