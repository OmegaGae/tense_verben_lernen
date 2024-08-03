-- Database of VerbenLernen Application for creation

-- create database
CREATE DATABASE VerbenLernen;
USE VerbenLernen;

-- create database tables/ schema as described by EPR defined in README
CREATE TABLE VerbenLernen(
    number INT AUTO_INCREMENT,
    infinitive VARCHAR(30) NOT NULL,
    present VARCHAR(30) NOT NULL,
    perfect VARCHAR(30) NOT NULL,
    auxiliary VARCHAR(10) NOT NULL,
    preterit VARCHAR(30) NOT NULL,
    level VARCHAR(2) NOT NULL,
    english_definition VARCHAR(100) NOT NULL,
    PRIMARY KEY(number)
);

-- Player table
CREATE TABLE Player(
    surname VARCHAR(30),
    current_level VARCHAR(2) DEFAULT('Unknown'),
    last_score INT DEFAULT(0),
    PRIMARY KEY(surname)
);

-- data of VerbenLernen table
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('beginnen', 'beginnt', 'begann', 'hat', 'begonnen', 'A1', 'to_begin');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bleiben', 'bleibt', 'blieb', 'ist', 'geblieben', 'A1', 'to_stay');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bringen', 'bringt', 'brachte', 'hat', 'gebracht', 'A1', 'to_stay');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('denken', 'denkt', 'dachte', 'hat', 'gedacht', 'A1', 'to_think');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('dürfen', 'darf', 'durfte', 'hat', 'gedurft', 'A1', 'to_be_allowed');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('essen', 'isst', 'aß', 'hat', 'gegessen', 'A1', 'to_eat');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fahren', 'fährt', 'fuhr', 'hat/ist', 'gefahren', 'A1', 'to_drive');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fangen', 'fängt', 'fing', 'hat', 'gefangen', 'A1', 'to_catch');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('finden', 'findet', 'fand', 'hat', 'gefunden', 'A1', 'to_find');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fliegen', 'fliegt', 'flog', 'hat/ist', 'geflogen', 'A1', 'to_fly');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('geben', 'gibt', 'gab', 'hat', 'gegeben', 'A1', 'to_give');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gehen', 'geht', 'ging', 'ist', 'gegangen', 'A1', 'to_go');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('haben', 'hat', 'hatte', 'hat', 'gehabt', 'A1', 'to_have');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('heißen', 'heißt', 'hieß', 'hat', 'geheißen', 'A1', 'to_be_called');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('helfen', 'hilft', 'half', 'hat', 'geholfen', 'A1', 'to_help');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('kennen', 'kennt', 'kannte', 'hat', 'gekannt', 'A1', 'to_know_(be_familiar_with)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('kommen', 'kommt', 'kam', 'ist', 'gekommen', 'A1', 'to_come');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('können', 'kann', 'konnte', 'hat', 'gekonnt', 'A1', 'to_be_able_(can)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('lesen', 'liest', 'las', 'hat', 'gelesen', 'A1', 'to_read');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('mögen', 'mag', 'mochte', 'hat', 'gemocht', 'A1', 'to_like');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('müssen', 'muss', 'musste', 'hat', 'gemusst', 'A1', 'to_have_to_(must)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('nehmen', 'nimmt', 'nahm', 'hat', 'genommen', 'A1', 'to_take');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('rufen', 'ruft', 'rief', 'hat', 'gerufen', 'A1', 'to_call');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schlafen', 'schläft', 'schlief', 'hat', 'geschlafen', 'A1', 'to_sleep');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schreiben', 'schreibt', 'schrieb', 'hat', 'geschrieben', 'A1', 'to_write');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schwimmen', 'schwimmt', 'schwamm', 'hat/ist', 'geschwommen', 'A1', 'to_swim');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sehen', 'sieht', 'sah', 'hat', 'gesehen', 'A1', 'to_see');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sein', 'ist', 'war', 'ist', 'gewesen', 'A1', 'to_be');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('singen', 'singt', 'sang', 'hat', 'gesungen', 'A1', 'to_sing');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sollen', 'soll', 'sollte', 'hat', 'gesollt', 'A1', 'to_ought_to_(should)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sprechen', 'spricht', 'sprach', 'hat', 'gesprochen', 'A1', 'to_speak');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('stehen', 'steht', 'stand', 'hat', 'gestanden', 'A1', 'to_stand');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('treffen', 'trifft', 'traf', 'hat', 'getroffen', 'A1', 'to_meet');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('trinken', 'trinkt', 'trank', 'hat', 'getrunken', 'A1', 'to_drink');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('tun', 'tut', 'tat', 'hat', 'getan', 'A1', 'to_do');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('wissen', 'weiß', 'wusste', 'hat', 'gewusst', 'A1', 'to_know_(a_fact)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('wollen', 'will', 'wollte', 'hat', 'gewollt', 'A1', 'to_want');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('backen', 'backt', 'buk', 'hat', 'gebacken', 'A2', 'to_bake');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('biegen', 'biegt', 'bog', 'hat/ist', 'gebogen', 'A2', 'to_bend');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bieten', 'bietet', 'bot', 'hat', 'geboten', 'A2', 'to_offer');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bitten', 'bittet', 'bat', 'hat', 'gebeten', 'A2', 'to_request');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('braten', 'brät', 'briet', 'hat', 'gebraten', 'A2', 'to_fry');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fallen', 'fällt', 'fiel', 'ist', 'gefallen', 'A2', 'to_fall');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gefallen', 'gefällt', 'gefiel', 'hat', 'gefallen', 'A2', 'to_like,_to_please_(most_used),_to_favour');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gewinnen', 'gewinnt', 'gewann', 'hat', 'gewonnen', 'A2', 'to_win');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('laden', 'lädt', 'lud', 'hat', 'geladen', 'A2', 'to_load,_to_download');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('laufen', 'läuft', 'lief', 'ist', 'gelaufen', 'A2', 'to_run,_to_walk');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('liegen', 'liegt', 'lag', 'hat', 'gelegen', 'A2', 'to_lie_(lie_down)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('nennen', 'nennt', 'nannte', 'hat', 'genannt', 'A2', 'to_name,_to_call');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('rennen', 'rennt', 'rannte', 'ist', 'gerannt', 'A2', 'to_run');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('riechen', 'riecht', 'roch', 'hat', 'gerochen', 'A2', 'to_smell');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schließen', 'schließt', 'schloss', 'hat', 'geschlossen', 'A2', 'to_close');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sitzen', 'sitzt', 'saß', 'hat', 'gesessen', 'A2', 'to_sit');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('steigen', 'steigt', 'stieg', 'ist', 'gestiegen', 'A2', 'to_climb_(to_get_in),_to_mount');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sterben', 'stirbt', 'starb', 'ist', 'gestorben', 'A2', 'to_die');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('treiben', 'treibt', 'trieb', 'hat/ist', 'getrieben', 'A2', 'to_compel,_to_drive');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('vergessen', 'vergisst', 'vergaß', 'hat', 'vergessen', 'A2', 'to_forget');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('verlieren', 'verliert', 'verlor', 'hat', 'verloren', 'A2', 'to_lose');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('wachsen', 'wächst', 'wuchs', 'ist', 'gewachsen', 'A2', 'to_grow');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('waschen', 'wäscht', 'wusch', 'hat', 'gewaschen', 'A2', 'to_wash');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('werden', 'wird', 'wurde', 'ist', 'geworden', 'A2', 'to_become');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('werfen', 'wirft', 'warf', 'hat', 'geworfen', 'A2', 'to_throw');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('ziehen', 'zieht', 'zog', 'hat/ist', 'gezogen', 'A2', 'to_pull,_to_move');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('befehlen', 'befiehlt', 'befahl', 'hat', 'befohlen', 'B1', 'to_command');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('beißen', 'beißt', 'biss', 'hat', 'gebissen', 'B1', 'to_bite');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('binden', 'bindet', 'band', 'hat', 'gebunden', 'B1', 'to_bind');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('brechen', 'bricht', 'brach', 'hat/ist', 'gebrochen', 'B1', 'to_break');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('brennen', 'brennt', 'brannte', 'hat', 'gebrannt', 'B1', 'to_burn');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('empfehlen', 'empfiehlt', 'empfahl', 'hat', 'empfohlen', 'B1', 'to_recommend');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('erschrecken', 'erschrickt', 'erschrak', 'ist', 'erschrocken', 'B1', 'to_frighten,_to_be_startled');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fliehen', 'flieht', 'floh', 'ist', 'geflohen', 'B1', 'to_flee');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fließen', 'fließt', 'floss', 'ist', 'geflossen', 'B1', 'to_flow');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fressen', 'frisst', 'fraß', 'hat', 'gefressen', 'B1', 'to_devour_(eat_for_animals)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('frieren', 'friert', 'fror', 'hat/ist', 'gefroren', 'B1', 'to_freeze');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gelingen', 'gelingt', 'gelang', 'ist', 'gelungen', 'B1', 'to_be_successful');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gelten', 'gilt', 'galt', 'hat', 'gegolten', 'B1', 'to_pertain');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('genießen', 'genießt', 'genoss', 'hat', 'genossen', 'B1', 'to_enjoy');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('geschehen', 'geschieht', 'geschah', 'ist', 'geschehen', 'B1', 'to_happen');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gießen', 'gießt', 'goss', 'hat', 'gegossen', 'B1', 'to_pour');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gleichen', 'gleicht', 'glich', 'hat', 'geglichen', 'B1', 'to_resemble');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('graben', 'gräbt', 'grub', 'hat', 'gegraben', 'B1', 'to_dig');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('greifen', 'greift', 'griff', 'hat', 'gegriffen', 'B1', 'to_grasp');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('halten', 'hält', 'hielt', 'hat', 'gehalten', 'B1', 'to_hold,_to_stop');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('hängen', 'hängt', 'hing', 'hat', 'gehangen', 'B1', 'to_hang');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('heben', 'hebt', 'hob', 'hat', 'gehoben', 'B1', 'to_lift');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('klingen', 'klingt', 'klang', 'hat', 'geklungen', 'B1', 'to_sound_(it_sounds_good),_to_ring');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('lassen', 'lässt', 'ließ', 'hat', 'gelassen', 'B1', 'to_let');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('leiden', 'leidet', 'litt', 'hat', 'gelitten', 'B1', 'to_suffer');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('leihen', 'leiht', 'lieh', 'hat', 'geliehen', 'B1', 'to_lend,_to_borrow');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('lügen', 'lügt', 'log', 'hat', 'gelogen', 'B1', 'to_lie_(tell_a_falsehood)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('meiden', 'meidet', 'mied', 'hat', 'gemieden', 'B1', 'to_avoid');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('messen', 'misst', 'maß', 'hat', 'gemessen', 'B1', 'to_measure');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('raten', 'rät', 'riet', 'hat', 'geraten', 'B1', 'to_guess,_to_advise');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('reiben', 'reibt', 'rieb', 'hat', 'gerieben', 'B1', 'to_rub');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('reiten', 'reitet', 'ritt', 'hat/ist', 'geritten', 'B1', 'to_ride');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schaffen', 'schafft', 'schuf', 'hat', 'geschaffen', 'B1', 'to_create,_to_manage');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('scheiden', 'scheidet', 'schied', 'hat/ist', 'geschieden', 'B1', 'to_separate');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('scheinen', 'scheint', 'schien', 'hat', 'geschienen', 'B1', 'to_shine,_to_seem');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('scheißen', 'scheißt', 'schiss', 'hat', 'geschissen', 'B1', 'to_shit');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schieben', 'schiebt', 'schob', 'hat', 'geschoben', 'B1', 'to_push');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schießen', 'schießt', 'schoss', 'hat/ist', 'geschossen', 'B1', 'to_shoot');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schlagen', 'schlägt', 'schlug', 'hat', 'geschlagen', 'B1', 'to_hit,_to_strike');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schmeißen', 'schmeißt', 'schmiss', 'hat', 'geschmissen', 'B1', 'to_throw,_to_fling');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schneiden', 'schneidet', 'schnitt', 'hat', 'geschnitten', 'B1', 'to_cut');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schreien', 'schreit', 'schrie', 'hat', 'geschrien', 'B1', 'to_scream,_to_cry');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('senden', 'sendet', 'sandte', 'hat', 'gesandt', 'B1', 'to_send');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sinken', 'sinkt', 'sank', 'ist', 'gesunken', 'B1', 'to_sink');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('springen', 'springt', 'sprang', 'ist', 'gesprungen', 'B1', 'to_jump');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('stehlen', 'stiehlt', 'stahl', 'hat', 'gestohlen', 'B1', 'to_steal');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('stinken', 'stinkt', 'stank', 'hat', 'gestunken', 'B1', 'to_stink');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('streiten', 'streitet', 'stritt', 'hat', 'gestritten', 'B1', 'to_quarrel');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('tragen', 'trägt', 'trug', 'hat', 'getragen', 'B1', 'to_carry,_to_wear');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('treten', 'tritt', 'trat', 'hat/ist', 'getreten', 'B1', 'to_step');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('trügen', 'trügt', 'trog', 'hat', 'getrogen', 'B1', 'to_deceive');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('verzeihen', 'verzeiht', 'verzieh', 'hat', 'verziehen', 'B1', 'to_forgive');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('weisen', 'weist', 'wies', 'hat', 'gewiesen', 'B1', 'to_indicate');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('werben', 'wirbt', 'warb', 'hat', 'geworben', 'B1', 'to_advertise');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('wiegen', 'wiegt', 'wog', 'hat', 'gewogen', 'B1', 'to_weigh,_to_cradle');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('zwingen', 'zwingt', 'zwang', 'hat', 'gezwungen', 'B1', 'to_force');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bergen', 'birgt', 'barg', 'hat', 'geborgen', 'B2', 'to_rescue');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('blasen', 'bläst', 'blies', 'hat', 'geblasen', 'B2', 'to_blow');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gebären', 'gebärt', 'gebar', 'hat', 'geboren', 'B2', 'to_bear_(to_give_birth)');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('pfeifen', 'pfeift', 'pfiff', 'hat', 'gepfiffen', 'B2', 'to_whistle');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('reißen', 'reißt', 'riss', 'hat', 'gerissen', 'B2', 'to_rip');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('ringen', 'ringt', 'rang', 'hat', 'gerungen', 'B2', 'to_struggle');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('saufen', 'säuft', 'soff', 'hat', 'gesoffen', 'B2', 'to_guzzle,_to_tipple');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schmelzen', 'schmilzt', 'schmolz', 'hat/ist', 'geschmolzen', 'B2', 'to_melt');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schreiten', 'schreitet', 'schritt', 'ist', 'geschritten', 'B2', 'to_stride,_to_step');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schweigen', 'schweigt', 'schwieg', 'hat', 'geschwiegen', 'B2', 'to_be_silent');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schwellen', 'schwillt', 'schwoll', 'ist', 'geschwollen', 'B2', 'to_swell');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schwinden', 'schwindet', 'schwand', 'ist', 'geschwunden', 'B2', 'to_fade,_to_disappear');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schwören', 'schwört', 'schwor', 'hat', 'geschworen', 'B2', 'to_swear');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('spinnen', 'spinnt', 'spann', 'hat', 'gesponnen', 'B2', 'to_spin,_to_be_crazy');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('stechen', 'sticht', 'stach', 'hat', 'gestochen', 'B2', 'to_stab,_to_prick');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('stoßen', 'stößt', 'stieß', 'hat/ist', 'gestoßen', 'B2', 'to_bump');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('streichen', 'streicht', 'strich', 'hat/ist', 'gestrichen', 'B2', 'to_cancel,_to_delete');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('verderben', 'verdirbt', 'verdarb', 'hat/ist', 'verdorben', 'B2', 'to_spoil');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('weichen', 'weicht', 'wich', 'ist', 'gewichen', 'B2', 'to_yield,_to_give_way');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('wenden', 'wendet', 'wandte', 'hat', 'gewandt', 'B2', 'to_turn,_to_appeal_to');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('winden', 'windet', 'wand', 'hat', 'gewunden', 'B2', 'to_wind');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bewegen', 'bewegt', 'bewog', 'hat', 'bewogen', 'C1', 'to_move');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('dringen', 'dringt', 'drang', 'hat/ist', 'gedrungen', 'C1', 'to_get_through');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('erlöschen', 'erlischt', 'erlosch', 'ist', 'erloschen', 'C1', 'to_expire');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('fechten', 'ficht', 'focht', 'hat', 'gefochten', 'C1', 'to_fence');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gedeihen', 'gedeiht', 'gedieh', 'ist', 'gediehen', 'C1', 'to_thrive');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('genesen', 'genest', 'genas', 'ist', 'genesen', 'C1', 'to_recover');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('gleiten', 'gleitet', 'glitt', 'ist', 'geglitten', 'C1', 'to_glide');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('klimmen', 'klimmt', 'klomm', 'ist', 'geklommen', 'C1', 'to_climb');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('kneifen', 'kneift', 'kniff', 'hat', 'gekniffen', 'C1', 'to_pinch');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('kriechen', 'kriecht', 'kroch', 'ist', 'gekrochen', 'C1', 'to_crawl');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('melken', 'melkt', 'molk', 'hat', 'gemolken', 'C1', 'to_milk');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('preisen', 'preist', 'pries', 'hat', 'gepriesen', 'C1', 'to_praise');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('quellen', 'quillt', 'quoll', 'ist', 'gequollen', 'C1', 'to_well');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('rinnen', 'rinnt', 'rann', 'ist', 'geronnen', 'C1', 'to_trickle');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('saugen', 'saugt', 'sog', 'hat', 'gesogen', 'C1', 'to_suck,_to_vacuum');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schleichen', 'schleicht', 'schlich', 'ist', 'geschlichen', 'C1', 'to_sneak');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schleifen', 'schleift', 'schliff', 'hat', 'geschliffen', 'C1', 'to_grind');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schlingen', 'schlingt', 'schlang', 'hat', 'geschlungen', 'C1', 'to_loop,_to_gulp');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schwingen', 'schwingt', 'schwang', 'hat/ist', 'geschwungen', 'C1', 'to_sway,_to_wield');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sinnen', 'sinnt', 'sann', 'hat', 'gesonnen', 'C1', 'to_ponder');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('sprießen', 'sprießt', 'spross', 'ist', 'gesprossen', 'C1', 'to_sprout');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('wringen', 'wringt', 'wrang', 'hat', 'gewrungen', 'C1', 'to_wring');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bersten', 'birst', 'barst', 'ist', 'geborsten', 'C2', 'to_burst');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('bleichen', 'bleicht', 'blich', 'ist', 'geblichen', 'C2', 'to_bleach');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('dreschen', 'drischt', 'drosch', 'hat', 'gedroschen', 'C2', 'to_thrash');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('flechten', 'flicht', 'flocht', 'hat', 'geflochten', 'C2', 'to_weave');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('glimmen', 'glimmt', 'glomm', 'hat', 'geglommen', 'C2', 'to_glow');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('hauen', 'haut', 'hieb', 'hat', 'gehauen', 'C2', 'to_hit');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('schelten', 'schilt', 'schalt', 'hat', 'gescholten', 'C2', 'to_scold');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('scheren', 'schert', 'schor', 'hat', 'geschoren', 'C2', 'to_shear');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('speien', 'speit', 'spie', 'hat', 'gespien', 'C2', 'to_spit');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('stieben', 'stiebt', 'stob', 'hat/ist', 'gestoben', 'C2', 'to_fly,_to_spray');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('verdrießen', 'verdrießt', 'verdross', 'hat', 'verdrossen', 'C2', 'to_irritate,_to_annoy');
INSERT INTO VerbenLernen(infinitive,present,perfect,auxiliary,preterit,level,english_definition) VALUES('weben', 'webt', 'wob', 'hat', 'gewoben', 'C2', 'to_weave');

-- create Table level: A1_verben, A2_verben... as view 
CREATE VIEW A1_Verben AS SELECT * FROM VerbenLernen WHERE level='A1';
CREATE VIEW A2_Verben AS SELECT * FROM VerbenLernen WHERE level='A2';
CREATE VIEW B1_Verben AS SELECT * FROM VerbenLernen WHERE level='B1';
CREATE VIEW B2_Verben AS SELECT * FROM VerbenLernen WHERE level='B2';
CREATE VIEW C1_Verben AS SELECT * FROM VerbenLernen WHERE level='C1';
CREATE VIEW C2_Verben AS SELECT * FROM VerbenLernen WHERE level='C2';