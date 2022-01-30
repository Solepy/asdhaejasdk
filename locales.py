from locales_dict import Locale, LocalesDict

locale_en = Locale()
locale_ru = Locale()
locale_uk = Locale()
locale_de = Locale()
locale_it = Locale()

locales = LocalesDict({
    'en': locale_en,
    'ru': locale_ru,
    'uk': locale_uk,
    'de': locale_de,
    'it': locale_it
}, locale_en)

# TOO_LONG_TITLE
locale_it.too_long_title = 'Il tuo messaggio è troppo lungo'

# FOR_TITLE
locale_it.for_title = 'Messaggio per %s'

# EXCEPT_TITLE
locale_it.except_title = 'Messaggio per tutti tranne %s'

# SPOILER_TITLE
locale_it.spoiler_title = 'Spoiler'

# TOO_LONG_MESSAGE
locale_it.too_long_message = 'Mi dispiace, il tuo messaggio non può essere inviato, poichè supera il limite di 200 caratteri.'

# FOR_MESSAGE
locale_it.for_message = '💬 Messaggio privato per %s, solo lui/lei potrà visualizzarlo.'

# EXCEPT_MESSAGE
locale_it.except_message = '💬 Messaggio privato per tutti tranne %s, solo lui/lei NON potrà visualizzarlo.'

# SPOILER_MESSAGE
locale_it.spoiler_message = '💬 Messaggio contenente spoiler, visualizzare coscientemente.'

# GROUP_GREETING_MESSAGE
locale_it.group_greeting_message = (
        '👋 Ciao! Il mio nome è %s e posso aiutarti ad inviare messaggi privati che solo alcuni potranno visualizzare. '
        'per sapere di più invia /start@%s e sentiti libero di chiedere aiuto'
        '<a href="t.me/orfeo"> se hai domande.')

# INFO_MESSAGE
locale_it.info_message = (
         'Se hai domande puoi contattarmi!'💬 \n\n'
        
         'Contact: @orfeo')

# HOW_TO_USE
locale_it.how_to_use = 'Come usare questo bot?'

# TOO_LONG_DESCRIPTION
locale_it.too_long_description = 'Perfavore accorcia la lunghezza del tuo messaggio in modo che non superi i 200 caratteri.'

# NOT_ALLOWED
locale_it.not_allowed = 'Non hai il permesso per leggere questo messaggio.'

# NOT_ACCESSIBLE
locale_it.not_accessible = 'Questo contenuto non è più visualizzabile.'

# VIEW
locale_it.view = 'Leggi'

# AND_CONNECTOR
locale_it.and_connector = 'e'
