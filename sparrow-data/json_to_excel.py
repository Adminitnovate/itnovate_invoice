import pandas as pd
import json

data = []
with open('docs/models/donut/data/img/train/metadata.jsonl', 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        gt_parse = json.loads(json_obj['ground_truth'])

        header = gt_parse.get('gt_parse', {}).get('header', {})  # Handle missing 'header' field
        items = gt_parse.get('gt_parse', {}).get('items', [])
        summary = gt_parse.get('gt_parse', {}).get('summary', {})

        item_desc = ', '.join([item.get('item_desc', '') for item in items])
        item_qty = ', '.join([item.get('item_qty', '') for item in items])
        item_net_price = ', '.join([item.get('item_net_price', '') for item in items])
        item_net_worth = ', '.join([item.get('item_net_worth', '') for item in items])
        item_vat = ', '.join([item.get('item_vat', '') for item in items])
        item_gross_worth = ', '.join([item.get('item_gross_worth', '') for item in items])

        data.append({

            'invoice_no': header.get('invoice_no', ''),
            'invoice_date': header.get('invoice_date', ''),
            'seller': header.get('seller', ''),
            'client': header.get('client', ''),
            'seller_tax_id': header.get('seller_tax_id', ''),
            'client_tax_id': header.get('client_tax_id', ''),
            'iban': header.get('iban', ''),
            'item_desc': item_desc,
            'item_qty': item_qty,
            'item_net_price': item_net_price,
            'item_net_worth': item_net_worth,
            'item_vat': item_vat,
            'item_gross_worth': item_gross_worth,
            'total_net_worth': summary.get('total_net_worth', ''),
            'total_vat': summary.get('total_vat', ''),
            'total_gross_worth': summary.get('total_gross_worth', ''),
            'file_name': json_obj.get('file_name', '')
        })

df = pd.DataFrame(data)
print(df)


df.to_excel('docs/models/donut/data/output.xlsx', index=False)

