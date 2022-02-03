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
locale_en.too_long_title = 'Your message is too long'

# FOR_TITLE
locale_it.for_title = 'Messaggio per %s'
locale_en.for_title = 'Message for %s'

# EXCEPT_TITLE
locale_it.except_title = 'Messaggio per tutti tranne %s'
locale_en.except_title = 'Message for everyone except %s'

# SPOILER_TITLE
locale_it.spoiler_title = 'Spoiler'
locale_en.spoiler_title = 'Spoiler'

# TOO_LONG_MESSAGE
locale_it.too_long_message = 'Mi dispiace, il tuo messaggio non può essere inviato, poichè supera il limite di 200 caratteri.'
locale_en.too_long_message = 'I am sorry, your message could not be sent, because exceeds the limit of 200 characters'

# FOR_MESSAGE
locale_it.for_message = '💬 Messaggio privato per %s, solo lui/lei potrà visualizzarlo.'
locale_en.for_message = '💬 Private message for %s only he/she can view it.'

# EXCEPT_MESSAGE
locale_it.except_message = '💬 Messaggio privato per tutti tranne %s, solo lui/lei NON potrà visualizzarlo.'
locale_en.except_message = '💬 Private message for everyone except %s, only he/she will not be able to view it.'

# SPOILER_MESSAGE
locale_it.spoiler_message = '💬 Il messaggio potrebbe contenere spoiler, visualizzare coscientemente.'
locale_en.spoiler_message = '💬 The message may contain a spoiler, view consciously.'

# GROUP_GREETING_MESSAGE
locale_it.group_greeting_message = (
        '👋 Ciao! Il mio nome è %s e posso aiutarti ad inviare messaggi privati che solo alcuni potranno visualizzare. '
        'per sapere di più invia /start@%s e sentiti libero di chiedere aiuto'
        '<a href="t.me/orfeo"> se hai domande.')

# INFO_MESSAGE
locale_it.info_message = (
         'Ciao! 🇮🇹\n\n@ppvtbot ti permette di inviare messaggi segreti nei gruppi, che solo il destinatario da te selezionato potrà visualizzare! ⚙️\n\nI messaggi che invierai non saranno accessibili a nessun altro. Solo chi lo ha scritto e il destinatario potranno visualizzarli. Ci tengo a specificare che il creatore del bot non ha accesso a codesti messaggi, e non ha dunque la possibilità di leggerli. 🔏\n\nInoltre il bot offre altre due opzioni, una per gli spoiler, ed una per mandare un messaggio che sarà leggibile da tutti tranne che da una persona, sarai tu a decidere chi. 💬\n\nIl bot è ancora in fase di sviluppo, per qualsiasi problema puoi contattarmi. ⌨️\n\nContact: @orfeo')
locale_en.info_message = (
         'Hello! 🇬🇧\n\n@ppvtbot allows you to send secret messages in groups, wich only the recipient you select will be able to view! ⚙️\n\nThe messages you send will not be accessible to anyone else. Only those who wrote it and the recipient will be able to view them. I want to specify that the creator of the bot does not have access to these messages, and therefore does not have the possibility to read them. 🔏\n\nFurthermore the bot offers two other options, first one for spoilers, and second one sending a message that will be readeable by everyone except one person, you decide who. 💬\n\nThe bot is still under development, for any problem you can contact me. ⌨️\n\nContact: @orfeo '
)

# HOW_TO_USE
locale_it.how_to_use = 'Come usare questo bot?'
locale_en.how_to_use = 'How to use this bot?' 

# TOO_LONG_DESCRIPTION
locale_it.too_long_description = 'Perfavore accorcia la lunghezza del tuo messaggio in modo che non superi i 200 caratteri.'
locale_en.too_long_description = 'Please shorten the length of your message so that it does not exceed 200 characters.'

# NOT_ALLOWED
locale_it.not_allowed = 'Non hai il permesso per leggere questo messaggio. 🔐' 
locale_en.not_allowed = 'You do not have permission to read this message. 🔐'

# NOT_ACCESSIBLE
locale_it.not_accessible = 'Questo contenuto non è più visualizzabile.'
locale_en.not_accessible = 'This content is no longer viewable.'

# VIEW
locale_it.view = 'Leggi 🔒 '
locale_en.view = 'Read 🔒'

# AND_CONNECTOR
locale_it.and_connector = 'e'
locale_en.and_connector = 'and'
