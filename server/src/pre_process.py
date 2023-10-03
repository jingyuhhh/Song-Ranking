import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ASSETS_PATH = '../client/src/assets/'


def pre_process(df_train: pd.DataFrame, positive_word: pd.DataFrame, df_feature: pd.DataFrame):
    pd.options.mode.chained_assignment = None
    positive_word.columns = ['char', 'word_set']
    positive_word['word_set'] = positive_word['word_set'].apply(
        lambda r: set([word.strip().lower for word in r.split(',')]))
    print('Column List {}'.format(df_train.columns.tolist()))
    print('There are # row {}, #col {}'.format(df_train.shape[0], df_train.shape[1]))
    df_train['Date'] = pd.to_datetime(df_train['Date'])
    df_train = df_train.loc[df_train.Date.dt.year == 2017, :]
    df_train['month'] = df_train.Date.dt.month
    df_train['day'] = df_train.Date.dt.day
    df_train['dayofweek'] = df_train.Date.dt.dayofweek
    print('-------------------------------------------------------')
    print('Positive Word sample')
    print(positive_word.sample(1))
    list_country = [{"AD", "Andorra"},
                    {"AE", "United Arab Emirates"},
                    {"AF", "Afghanistan"},
                    {"AG", "Antigua and Barbuda"},
                    {"AI", "Anguilla"},
                    {"AL", "Albania"},
                    {"AM", "Armenia"},
                    {"AO", "Angola"},
                    {"AQ", "Antarctica"},
                    {"AR", "Argentina"},
                    {"AS", "American Samoa"},
                    {"AT", "Austria"},
                    {"AU", "Australia"},
                    {"AW", "Aruba"},
                    {"AX", "Åland Islands"},
                    {"AZ", "Azerbaijan"},
                    # B
                    {"BA", "Bosnia and Herzegovina"},
                    {"BB", "Barbados"},
                    {"BD", "Bangladesh"},
                    {"BE", "Belgium"},
                    {"BF", "Burkina Faso"},
                    {"BG", "Bulgaria"},
                    {"BH", "Bahrain"},
                    {"BI", "Burundi"},
                    {"BJ", "Benin"},
                    {"BL", "Saint Barthélemy"},
                    {"BM", "Bermuda"},
                    {"BN", "Brunei Darussalam"},
                    {"BO", "Bolivia, Plurinational State of"},
                    {"BQ", "Bonaire, Sint Eustatius and Saba"},
                    {"BR", "Brazil"},
                    {"BS", "Bahamas"},
                    {"BT", "Bhutan"},
                    {"BV", "Bouvet Island"},
                    {"BW", "Botswana"},
                    {"BY", "Belarus"},
                    {"BZ", "Belize"},
                    # C
                    {"CA", "Canada"},
                    {"CC", "Cocos (Keeling) Islands"},
                    {"CD", "Congo, the Democratic Republic of"},
                    {"CF", "Central African Republic"},
                    {"CG", "Congo"},
                    {"CH", "Switzerland"},
                    {"CI", "Côte d'Ivoire"},
                    {"CK", "Cook Islands"},
                    {"CL", "Chile"},
                    {"CM", "Cameroon"},
                    {"CN", "China"},
                    {"CO", "Colombia"},
                    {"CR", "Costa Rica"},
                    {"CU", "Cuba"},
                    {"CV", "Cabo Verde"},
                    {"CW", "Curaçao"},
                    {"CX", "Christmas Island"},
                    {"CY", "Cyprus"},
                    {"CZ", "Czech Republic"},
                    # D
                    {"DE", "Germany"},
                    {"DJ", "Djibouti"},
                    {"DK", "Denmark"},
                    {"DM", "Dominica"},
                    {"DO", "Dominican Republic"},
                    {"DZ", "Algeria"},
                    # E
                    {"EC", "Ecuador"},
                    {"EE", "Estonia"},
                    {"EG", "Egypt"},
                    {"EH", "Western Sahara"},
                    {"ER", "Eritrea"},
                    {"ES", "Spain"},
                    {"ET", "Ethiopia"},
                    # F
                    {"FI", "Finland"},
                    {"FJ", "Fiji"},
                    {"FK", "Falkland Islands (Malvinas)"},
                    {"FM", "Micronesia, Federated States of"},
                    {"FO", "Faroe Islands"},
                    {"FR", "France"},
                    # G
                    {"GA", "Gabon"},
                    {"GB", "United Kingdom of Great Britain and Northern Ireland"},
                    {"GD", "Grenada"},
                    {"GE", "Georgia"},
                    {"GF", "French Guiana"},
                    {"GG", "Guernsey"},
                    {"GH", "Ghana"},
                    {"GI", "Gibraltar"},
                    {"GL", "Greenland"},
                    {"GM", "Gambia"},
                    {"GN", "Guinea"},
                    {"GP", "Guadeloupe"},
                    {"GQ", "Equatorial Guinea"},
                    {"GR", "Greece"},
                    {"GS", "South Georgia and the South Sandwich Islands"},
                    {"GT", "Guatemala"},
                    {"GU", "Guam"},
                    {"GW", "Guinea-Bissau"},
                    {"GY", "Guyana"},
                    # H
                    {"HK", "Hong Kong"},
                    {"HM", "Heard Island and McDonalds Islands"},
                    {"HN", "Honduras"},
                    {"HR", "Croatia"},
                    {"HT", "Haiti"},
                    {"HU", "Hungary"},
                    # I
                    {"ID", "Indonesia"},
                    {"IE", "Ireland"},
                    {"IL", "Israel"},
                    {"IM", "Isle of Man"},
                    {"IN", "India"},
                    {"IO", "British Indian Ocean Territory"},
                    {"IQ", "Iraq"},
                    {"IR", "Iran, Islamic Republic of"},
                    {"IS", "Iceland"},
                    {"IT", "Italy"},
                    # J
                    {"JE", "Jersey"},
                    {"JM", "Jamaica"},
                    {"JO", "Jordan"},
                    {"JP", "Japan"},
                    # K
                    {"KE", "Kenya"},
                    {"KG", "Kyrgyzstan"},
                    {"KH", "Cambodia"},
                    {"KI", "Kiribati"},
                    {"KM", "Comoros"},
                    {"KN", "Saint Kitts and Nevis"},
                    {"KP", "Korea, Democratic People's Republic of"},
                    {"KR", "Korea, Republic of"},
                    {"KW", "Kuwait"},
                    {"KY", "Cayman Islands"},
                    {"KZ", "Kazakhstan"},
                    # L
                    {"LA", "Lao People's Democratic Republic"},
                    {"LB", "Lebanon"},
                    {"LC", "Saint Lucia"},
                    {"LI", "Liechtenstein"},
                    {"LK", "Sri Lanka"},
                    {"LR", "Liberia"},
                    {"LS", "Lesotho"},
                    {"LT", "Lithuania"},
                    {"LU", "Luxembourg"},
                    {"LV", "Latvia"},
                    # M
                    {"MA", "Morocco"},
                    {"MC", "Monaco"},
                    {"MD", "Moldova, Republic of"},
                    {"ME", "Montenegro"},
                    {"MF", "Saint Martin (French part)"},
                    {"MG", "Madagascar"},
                    {"MH", "Marshall Islands"},
                    {"MK", "Macedonia, the former Yugoslav Republic of"},
                    {"ML", "Mali"},
                    {"MM", "Myanmar"},
                    {"MN", "Mongolia"},
                    {"MO", "Macao"},
                    {"MP", "Northern Mariana Islands"},
                    {"MQ", "Martinique"},
                    {"MR", "Mauritania"},
                    {"MS", "Montserrat"},
                    {"MT", "Malta"},
                    {"MU", "Mauritius"},
                    {"MV", "Maldives"},
                    {"MW", "Malawi"},
                    {"MX", "Mexico"},
                    {"MY", "Malaysia"},
                    {"MZ", "Mozambique"},
                    # N
                    {"NA", "Namibia"},
                    {"NC", "New Caledonia"},
                    {"NE", "Niger"},
                    {"NF", "Norfolk Island"},
                    {"NG", "Nigeria"},
                    {"NI", "Nicaragua"},
                    {"NL", "Netherlands"},
                    {"NO", "Norway"},
                    {"NP", "Nepal"},
                    {"NR", "Nauru"},
                    {"NU", "Niue"},
                    {"NZ", "New Zealand"},
                    # O
                    {"OM", "Oman"},
                    # P
                    {"PA", "Panama"},
                    {"PE", "Peru"},
                    {"PF", "French Polynesia"},
                    {"PG", "Papua New Guinea"},
                    {"PH", "Philippines"},
                    {"PK", "Pakistan"},
                    {"PL", "Poland"},
                    {"PM", "Saint Pierre and Miquelon"},
                    {"PN", "Pitcairn"},
                    {"PR", "Puerto Rico"},
                    {"PS", "Palestine, State of"},
                    {"PT", "Portugal"},
                    {"PW", "Palau"},
                    {"PY", "Paraguay"},
                    # Q
                    {"QA", "Qatar"},
                    # R
                    {"RE", "Réunion"},
                    {"RO", "Romania"},
                    {"RS", "Serbia"},
                    {"RU", "Russian Federation"},
                    {"RW", "Rwanda"},
                    # S
                    {"SA", "Saudi Arabia"},
                    {"SB", "Solomon Islands"},
                    {"SC", "Seychelles"},
                    {"SD", "Sudan"},
                    {"SE", "Sweden"},
                    {"SG", "Singapore"},
                    {"SH", "Saint Helena, Ascension and Tristan da Cunha"},
                    {"SI", "Slovenia"},
                    {"SJ", "Svalbard and Jan Mayen"},
                    {"SK", "Slovakia"},
                    {"SL", "Sierra Leone"},
                    {"SM", "San Marino"},
                    {"SN", "Senegal"},
                    {"SO", "Somalia"},
                    {"SR", "Suriname"},
                    {"SS", "South Sudan"},
                    {"ST", "Sao Tome and Principe"},
                    {"SV", "El Salvador"},
                    {"SX", "Sint Maarten (Dutch part)"},
                    {"SY", "Syrian Arab Republic"},
                    {"SZ", "Swaziland"},
                    # T
                    {"TC", "Turks and Caicos Islands"},
                    {"TD", "Chad"},
                    {"TF", "French Southern Territories"},
                    {"TG", "Togo"},
                    {"TH", "Thailand"},
                    {"TJ", "Tajikistan"},
                    {"TK", "Tokelau"},
                    {"TL", "Timor-Leste"},
                    {"TM", "Turkmenistan"},
                    {"TN", "Tunisia"},
                    {"TO", "Tonga"},
                    {"TR", "Turkey"},
                    {"TT", "Tuvalu"},
                    {"TW", "Taiwan, Province of China"},
                    {"TZ", "Tanzania, United Republic of"},
                    # U
                    {"UA", "Ukraine"},
                    {"UG", "Uganda"},
                    {"UM", "United States Minor Outlying Islands"},
                    {"US", "United States of America"},
                    {"UY", "Uruguay"},
                    {"UZ", "Uzbekistan"},
                    # V
                    {"VA", "Holy See"},
                    {"VC", "Saint Vincent and the Grenadines"},
                    {"VE", "Venezuela, Bolivarian Republic of"},
                    {"VG", "Virgin Islands, British"},
                    {"VI", "Virgin Islands, U.S."},
                    {"VN", "Viet Nam"},
                    {"VU", "Vanuatu"},
                    # W
                    {"WF", "Wallis and Futuna"},
                    {"WS", "Samoa"},
                    # Y
                    {"YE", "Yemen"},
                    {"YT", "Mayotte"},
                    # Z
                    {"ZA", "South Africa"},
                    {"ZM", "Zambia"},
                    {"ZW", "Zimbabwe"}]
    dict_count = {(full.lower() if len(abv) > len(full) else abv.lower()): (abv if len(abv) > len(full) else full) for
                  abv, full in list_country}
    df_train['Region_full'] = df_train['Region'].map(dict_count)

    # Basic Auditing

    print('Where column has Null Value?')
    print(df_train.columns[df_train.isnull().any()].tolist())
    df_tmp = df_train[['Track Name', 'Artist', 'URL']].fillna('None')  # 用‘None’填充没有数据的地方
    df_train.dropna(inplace=True)
    tot = df_tmp.shape[0]
    ref = {}
    for i, name in enumerate(['Track Name', 'Artist', 'URL']):
        none_cnt = (df_tmp[name] == 'None').sum()
        ref[name] = [tot - none_cnt, none_cnt]
    ref = pd.DataFrame(ref)
    ref.iloc[1, :] / tot

    df_train.dropna(inplace=True)
    df_tmp = df_train.loc[df_train.Date.dt.year == 2017, :]
    for col in ['month', 'day', 'dayofweek']:
        plt.figure(figsize=(5, 4))
        ax = plt.subplot(1, 1, 1)
        cnt = df_tmp[col].value_counts()
        cnt.sort_index(inplace=True)
        sns.barplot(x=cnt.index, y=cnt.values, ax=ax)
        ax.set_title(col)
        ax.tick_params('x', rotation=90)
        plt.subplots_adjust(hspace=0.2, top=0.85)
        plt.suptitle('2017 Season Cnt')
        plt.savefig(ASSETS_PATH+'2017 ' + col + ' Cnt.png')

    month_user = df_train.loc[df_train.Date.dt.year == 2017, :].groupby('month')['Streams'].sum().to_frame()
    f, ax = plt.subplots(1, 2, figsize=(12, 3))
    ax[0].plot(np.arange(1, 13), month_user['Streams'], '-ro')
    ax[0].set_title('Number of Streams 2017 Month')
    country_per_month = df_train.loc[df_train.Date.dt.year == 2017, :].groupby('month')['Region'].nunique().to_frame()
    ax[1].plot(np.arange(1, 13), country_per_month['Region'], '-ro')
    ax[1].set_title('Number of Country 2017 Month')
    plt.savefig(ASSETS_PATH+'Number of Streams and Country 2017 Month')

    us_song = df_train.loc[df_train.Region == 'us', :]
    df_stream = us_song[['Date', 'Track Name', 'Streams', 'Position']]
    df_stream = df_stream.groupby(['Date', 'Track Name']).first().reset_index()
    stream_num = df_stream.pivot(index='Date', columns='Track Name', values='Streams')
    pos_num = df_stream.pivot(index='Date', columns='Track Name', values='Position')
    us_unique_song = us_song['Track Name'].loc[us_song.Position == 1].unique()


    def draw_stream_pos(us_unique_song, i, type_):
        song = us_unique_song[i]
        song_stream = stream_num.loc[:, song]
        song_pos = pos_num.loc[:, song]
        tmp = song_stream.loc[song_stream.notnull()]
        tmp2 = song_pos.loc[song_stream.notnull()]
        first = (tmp2.values == 1)
        not_first = ~first
        f, ax = plt.subplots(1, 2, figsize=(12, 4))
        ax[0].scatter(tmp.index[not_first], tmp.values[not_first], alpha=0.4, color='grey')
        ax[0].scatter(tmp.index[first], tmp.values[first], color='red')
        ax[1].scatter(tmp2.index[not_first], tmp2.values[not_first], alpha=0.4, color='grey')
        ax[1].scatter(tmp2.index[first], tmp2.values[first], color='red')
        ax[1].invert_yaxis()
        ax[1].set_title('Top1 Number : ' + str((tmp2.values == 1).sum()))
        ax[0].set_title(type_ + ': ' + song)
        plt.savefig(ASSETS_PATH+type_+'.png')

    type_of_graph = {0: 'Up_Down', 2: 'Down', 3: 'Alone Down', 4: 'Sudden SoarUp', 5: 'Remix', 6: 'Down Mean', 8: 'Curve'}
    for key, type_ in type_of_graph.items():
        draw_stream_pos(us_unique_song, key, type_)
