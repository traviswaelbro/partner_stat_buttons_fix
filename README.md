# Partner Stat Buttons Fix

_partner_stat_buttons_fix_ fixes the _oe_stat_button_s to use more logical calculations. 

For Sales & Quotes counters, this means the buttons will include sales & quotes from a partner's children (contacts) as well.
- It only goes one level down. So if you are on the company record, it will include all contacts' sales, but it will not include sales done by those contacts' addresses.

##### To Do:

- Test in default instance
- Rewrite in v8 API?
- Add improvement to Invoices button
  - Exclude cancelled invoices from totals
