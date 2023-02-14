# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define azuma = Character("AZUMA", image="azuma", color="#fff", kerning=2.5, namebox_background="gui/namebox/red.png" )
init python:
    renpy.music.register_channel("ambiance", "sfx", True)
    chess_script = os.path.join(renpy.config.gamedir, THIS_PATH , 'chess_subprocess.py')
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH , 'python-packages')

    startupinfo = None
    if renpy.windows:      
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW

    # remember to kill this process after use to prevent memory leak
    # but don't kill it unless there is no more chess game to play in your VN
    chess_subprocess = subprocess.Popen(
        [sys.executable, chess_script, import_dir],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        startupinfo=startupinfo)

default park_first = False
define m = Character("Mateus", namebox_background=AlphaMask(Solid("#d97fff"), "gui/namebox.png"))
define c = Character("Constança", namebox_background=AlphaMask(Solid("#ff7ff0"), "gui/namebox.png"))
define igor = Character("Igor", namebox_background=AlphaMask(Solid("#746bff"), "gui/namebox.png"))
define n = Character("Mateus Escritor", namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
image urban night 1 = Movie(size=(1920, 1080), play="images/urban night 1.webm")
image urban 2 = Movie(size=(1920, 1080), play="images/urban 2.webm")
image urban 3 = Movie(size=(1920, 1080), play="images/urban 3.webm")
image rural 3 = Movie(size=(1920, 1080), play="images/rural 3.webm")
image rural 1 = Movie(size=(1920, 1080), play="images/rural 1.webm")
image mateus 1 = im.Scale("images/mateus 1.png", 466, 840)
image mateus 1 wink = im.Scale("images/mateus 1 wink.png", 466, 840)
image mateus 2 = im.Scale("images/mateus 2.png", 466, 840)
image mateus 2 wink = im.Scale("images/mateus 2 wink.png", 466, 840)
image mateus grin = im.Scale("images/mateus grin.png", 466, 840)
image mateus grin wink = im.Scale("images/mateus grin wink.png", 466, 840)
image mateus sob = im.Scale("images/mateus sob.png", 466, 840)
image mateus sexo = im.Scale("images/mateus sexo.png", 466, 840)

# The game starts here.

label start:
    scene urban 2
    with dissolve

    play music "audio/vlc theme.wav" fadeout 0.5 fadein 0.5
    play ambiance "audio/vlc ambiance.mp3" fadeout 0.5 fadein 0.5

    "Depois de ter feito quase 300km para ir ter com o Mateus, eu estava finalmente a chegar a Vale de Cambra."
    "Só mais uns passos e eu iria finalmente poder abraçá-lo."
    "Eu toquei-lhe à campainha."
    "Depois de um longo abraço... finalmente trocámos as primeiras palavras."

    show mateus 2
    
    menu:

        "Deixo o Mateus falar?"

        "Sim":
            jump sim

        "Não":
            jump nao
       
    label sim:
        show mateus 2 wink
        m "Tu criaste um novo jogo com o Ren'Py!"
        m "Quando tiveres uma história, música e imagens, podes mostrá-lo ao mundo!!"
        "Mas que raio é que ele está a dizer hoje?"
        c "Boo... Está tudo bem?"
        m "Sim, está! Não sei donde é que tirei isto, as palavras saíram sozinhas!"
        "Mais uma vez, o Mateus está a falar sozinho, completamente sem sentido e sem reparar que o que disse foi estranho."
        "Mas eu já estou habituada a isto."
        jump post_sim

    label nao:
        c "Olá meu amor, como estás?"
        m "Estou bem, e tu?"
        c "Amo-te muito! Estou tão feliz por te ver!"
        jump post_sim

    label post_sim:
        c "Estás pronto para sair?"

    show mateus 2
    m "Sim, claro! Vamos! Tenho um date todo planeado! Hoje estás reservada para mim!"
    c "Obrigada, meu amor lindo esbelto e maravilhoso!"

    m "Obrigado, minha princesa linda e maravilhosa!"
    m "Primeira coisa, vamos à estação de comboios de Vale de Cambra."
    m "Quero levar-te a um lugar muito especial."

    scene rural 3
    with dissolve

    show mateus 1
    "Eu fui para a estação de comboios de Vale de Cambra com o Mateus."
    "Ele estava tão animado que eu não conseguia parar de sorrir."
    "Vimos muitos gatinhos pelo caminho, e eu não conseguia parar de os fotografar."
    "O passeio foi muito agradável, mas eu não sabia o que ele tinha planeado."

    play music igor fadeout 0.5 fadein 0.5

    show igor
    igor "Bem vindo à estação de comboios de Vale de Cambra..."
    igor "Este sítio localiza-se entre matéria e mente, entre sonho e realidade..."
    igor "Aqui, o tempo não passa, e o tempo não pára..."
    igor "O tempo é uma ilusão, e a ilusão é uma realidade..."
    igor "O seu bilhete, por favor..."
    hide igor

    play music "audio/vlc theme.wav" fadeout 0.5 fadein 0.5

    "O Mateus comprou os bilhetes para nós, para eu não saber onde íamos."
    
    c "Quem é aquele homem estranho?"
    show mateus grin
    m "É o meu primo, o Marco Igor António Tavares de Almeida, mas nós chamámos-lhe Igor."
    m "Ele é um pouco estranho, mas é muito querido."

    show igor at left with dissolve
    show mateus grin at right with dissolve
    "Ficamos a conversar com o Igor durante algum tempo enquanto esperávamos pelo comboio."
    "Ele gosta muito de ir às piscinas e de K-pop, mas é muito tímido e não gosta de falar com mulheres."
    
    show mateus grin with dissolve
    m "O comboio está a chegar!"
    m "Vamos, vamos!"

    stop music
    scene train
    play ambiance "audio/train.mp3" fadeout 0.5 fadein 0.5

    "Entrámos no comboio e estivemos algum tempo à procura de lugares."
    "Estivemos a conversar sobre tudo e sobre nada, e ainda consegui dormir um bocadinho."

    menu:
        
        "Durmo mais um bocadinho?"

        "Sim":
            "Eu dormi mais um bocadinho, e quando acordei, o Mateus estava a falar sozinho."
            "Ele estava a falar sobre um jogo que ele tinha criado com o Ren'Py."
            "Mas eu não estava a ouvir o que ele estava a dizer."
            jump nao_dormir

        "Não":
            "Estivemos a falar mais um bocado, até que..."
            jump nao_dormir

    label nao_dormir:
        show mateus sob with dissolve
        m "Mor... acho que apanhámos o comboio errado..."
        c "O que é que tu estás a dizer? Onde é que nós estamos?"
        m "Não sei, mas não é Arouca..."

    "Aiiii juro, o Mateus é tão estúpido!"
    "Eu não sei como é que eu consigo gostar dele."
    "Mas eu gosto dele, e não consigo mudar isso."
    "Eu não sei o que é que eu faria sem ele."

    m "Vamos sair aqui, acho que este comboio não vai para Arouca."

    scene rural 1
    with dissolve
    play music "audio/main theme.wav" fadeout 0.5 fadein 0.5
    play ambiance "audio/rebordosa ambiance.mp3" fadeout 0.5 fadein 0.5

    show mateus grin with dissolve
    "O Mateus saiu do comboio e eu fiquei a olhar para ele."
    "Eu estava um bocado zangada com ele, mas ele não reparou."
    "Ele estava a olhar para mim, e eu estava a olhar para ele."
    "Ele estava tão bonito, com o cabelo a cair-lhe sobre os olhos, e a sorrir para mim."
    "Eu não conseguia parar de o olhar, e ele não parava de me olhar também."
    "Eu não sei o que é que ele estava a pensar, mas eu estava a pensar que ele era o homem mais bonito do mundo."

    scene beijo with dissolve
    stop ambiance
    play music "audio/kiss.mp3" fadeout 0.5 fadein 0.5
    show mateus sexo with dissolve

    m "Chega aqui..."
    "O Mateus aproximou-se de mim e beijou-me."
    "Foi um beijo tão bom, tão quente, tão intenso, tão perfeito, tão doce."
    m "Eu amo-te muito! Desculpa ter me enganado no comboio."
    "O Mateus beijou-me outra vez, e eu beijei-o de volta."
    "Adoro estes beijos, e gostava que eles nunca acabassem."
    c "Quando chegarmos a casa, prometes-me que iremos ter mais beijos?"
    m "Sim! E talvez outras coisas também..."

    "O meu coração estava a bater de forma tão rápida que eu não conseguia respirar."

    scene rural 1 with dissolve
    play music "audio/main theme.wav" fadeout 0.5 fadein 0.5
    play ambiance "audio/rebordosa ambiance.mp3" fadeout 0.5 fadein 0.5

    show mateus 2
    m "Ora bem, vamos lá ver onde é que estamos..."
    m "Acho que estamos na Rebordosa!"
    
    c "Rebordosa, como a música do Chico da Tina!"
    show mateus grin with dissolve
    m "Sim, acho que é aqui!"

    "Consegui ver a felicidade no rosto do Mateus quando eu mencionei a música do Chico da Tina."
    show mateus 2 with dissolve
    m "Vamos dar um passeio aqui, e depois vamos para casa."
    m "Estive a ver no Google Maps e tem um parque muito bonito aqui perto com uma estátua de um gorila."
    m "Mas primeiro, vamos a um restaurante, que eu estou cheio de fome!"
    m "Também tens fome?"

    menu:
        "Tenho fome?"

        "Sim! Quero ir comer!":
            jump comer_já

        "Não, prefiro ir ver outras coisas!":
            jump outras_coisas

    label comer_já:
        c "Sim! Quero ir comer!"
        m "Ótimo! Vamos então!"
        jump restaurante

    label outras_coisas:
        c "Não, prefiro ir ver outras coisas!"
        m "Ok, vamos então ver o que é que há por aqui."
        $ park_first = True
        jump parque
    
    label restaurante:
        scene restaurante with dissolve
        play music "audio/restaurant theme.mp3" fadeout 0.5 fadein 0.5
        play ambiance "audio/restaurant ambiance.mp3" fadeout 0.5 fadein 0.5
        show mateus 1
        "Entrámos no restaurante e sentámo-nos numa mesa."
        m "O que é que tu queres comer?"
        c "Deixa me olhar para o menu... já sabes como é que eu sou."

    menu:
        "O que é que eu vou comer?"

        "Eu quero um bife com batatas fritas e uma salada.":
            jump bife

        "Eu quero comer choco frito com arroz de tomate.":
            jump choco

        "Eu quero comer umas sardinhas assadas com batatas cozidas.":
            jump sardinhas
    
    label bife:
        show mateus grin with dissolve
        m "Wow!!!! Que saboroso!"
        m "Eu vou comer salmão com salada e batatas fritas!"
        jump escolha_comida

    label choco:
        show mateus 1 wink with dissolve
        m "Sei que tu adoras choco frito!"
        m "Pena não ter pizza de choco aqui..."
        m "Eu vou comer salmão com salada e batatas fritas!"
        jump escolha_comida
    label sardinhas:
        show mateus 1
        m "Hmmm, escolha interessante!"
        m "Não estava à espera dessa..."
        m "Eu vou comer salmão com salada e batatas fritas!"
        jump escolha_comida

    label escolha_comida:
        "O nosso almoço foi muito bom, mas o Mateus bebeu a minha água sem eu me aperceber."
        "Eu não gosto de beber água, mas eu bebi um pouco para não o deixar mal."

    show mateus 2
    hide mateus 2
    show evil
    n "EU ACHEI BUÉ PIADA AO COPILOT TER ESCRITO ISTO DE NÃO BEBERES ÁGUA HAHAHAHAHA!"
    hide evil

    show mateus 2
    m "Gostaste do almoço?"

    menu:
        "O que é que eu vou dizer?"

        "Sim, foi muito bom!":
            jump bom

        "Não, foi horrível!":
            jump horrivel

        "Foi bom, mas não foi o melhor almoço que eu já comi.":
            jump bom

    label bom:
        show mateus grin with dissolve
        m "Eu também gostei muito!"
        jump post_almoço
    
    label horrivel:
        show mateus sob with dissolve
        m "Oh, desculpa..."
        m "Eu também não gostei muito..."
        jump post_almoço

    label post_almoço:
        if park_first:
            show mateus 2 with dissolve
            m "Acho que já comemos bastante, e eu quero descansar um bocadinho."
            m "Já está quase na hora de irmos para casa."
            m "Vamos indo para a estação de comboios?"
            "Começámos a caminhar para a estação de comboios e fomos para casa."
            jump casa
        else:
            show mateus 2 with dissolve
            m "Vamos dar um passeio pela Rebordosa?"
            m "O parque tem a estátua do gorila, e eu quero tirar uma foto lá!"
            jump parque

    label parque:
        scene urban 3 with dissolve
        play music "audio/main theme.wav" fadeout 0.5 fadein 0.5
        play ambiance "audio/rebordosa ambiance.mp3" fadeout 0.5 fadein 0.5
        show mateus grin with dissolve
        "O parque era bonito, mas não era tão bonito como o parque da cidade de Vale de Cambra."
        "Mas eu não disse nada, porque eu queria que o Mateus se sentisse bem."
        "Depois dele tirar a foto com a estátua do gorila, sentámo-nos num banco."
        m "O que é que tu achas deste parque?"
        c "É bonito, mas não é tão bonito como o parque da cidade de Vale de Cambra."
        m "Sim, eu também acho que não é tão bonito como o parque da cidade de Vale de Cambra."
        m "Mas eu gosto muito deste parque, e eu gosto de te ver feliz."
        c "Eu também gosto muito de ti, e eu gosto de te ver feliz."
        "Aproveitei para o beijar, enquanto ningém nos via."
        m "Eu amo-te muito!"
        c "Eu também te amo muito!"

        if park_first:
            show mateus 2 with dissolve
            "Trocamos mais uns beijos até que a barriga do Mateus começou a roncar."
            m "Eu estou com fome!"
            c "Queres ir ao restaurante então? A minha barriga também está a roncar!"
            "Começamos a caminhar até ao restaurante."
            jump restaurante
        else:
            show mateus 2 with dissolve
            "Trocamos mais uns beijos até que o sol se pôs."
            m "Vamos então para casa, que eu estou cansado."
            "Começamos a caminhar até à estação de comboios e fomos para casa."
            jump casa

    label casa:
        scene urban night 1 with dissolve
        stop music
        play ambiance "audio/night ambiance.mp3" fadeout 0.5 fadein 0.5
        "Chegámos à estação de comboios de Vale de Cambra."
        "Eu já estava muito cansada, mas eu queria fazer o que o Mateus queria."
        show mateus grin with dissolve
        m "Siga Dunas? Dunas hoje?"
        menu:
            "Dunas hoje?"

            "Sim, vamos ao Dunas!":
                show mateus grin with dissolve
                c "Sim, vamos ao Dunas!"
                m "OHHHH MY GOOOOOOD!!!!"
                jump dunas

            "Não, vamos para casa!":
                show mateus grin wink with dissolve
                c "Não, vamos para casa!"
                show mateus 2 with dissolveR
                m "Okay amor! Vamos dormir muito bem agarradinhos!"
                m "Eu amo-te muito!"
                jump dormir


    label dunas:
        scene dunas with dissolve
        play ambiance "audio/restaurant ambiance.mp3" fadeout 0.5 fadein 0.5
        play music "audio/dunas theme.wav" fadeout 0.5 fadein 0.5
        show mateus grin with dissolve
        m "Dunas Bar VLC!"
        m "Queres beber alguma coisa?"

        menu:
            "O que é que eu vou beber?"

            "Somersby!":
                c "Somersby!"
                m "Okay, vamos pedir duas Somersby!"
            
            "Margarita!":
                c "Margarita!"
                m "Okay, vamos pedir duas Margaritas!"

            "Não quero beber nada!":
                c "Não quero beber nada!"
                m "Okay, vamos pedir duas águas!"

        "Passado algum tempo, ouvi a barulha do Mateus a roncar, mesmo com a música alta do bar."
        m "Estou com fome..."
        m "Vou pedir um pires!"

        "O Mateus pediu um pires e comemos juntos."

        m "Estava mesmo bom!"
        c "Também achei!"
        m "Ah, lembrei me agora que o dunas tem um jogo de xadrez!"
        m "Queres jogar?"

        menu:
            "Quero jogar xadrez?"

            "Sim, vamos jogar!":
                show mateus grin with dissolve
                c "Sim, vamos jogar!"
                m "Let's gooo!"
                jump xadrez

            "Não, não quero jogar!":
                show mateus sob
                c "Não, não quero jogar!"
                m "Okay mor! Vamos ficar aqui só mais um bocadinho e depois vamos para casa!"
                jump igor

    label xadrez:
        # launches an easy-level PvC where player plays as white
        $ fen = STARTING_FEN
        $ movetime = 2000
        $ depth = 0
        $ player_color = WHITE
        window hide
        $ quick_menu = False
        # avoid rolling back and losing chess game state
        $ renpy.block_rollback()
        # disable Esc key menu to prevent the player from saving the game
        $ _game_menu_screen = None
        call screen chess(chess_subprocess, fen, player_color, movetime, depth)
        # re-enable the Esc key menu
        $ _game_menu_screen = 'save'
        # avoid rolling back and entering the chess game again
        $ renpy.block_rollback()
        # restore rollback from this point on
        $ renpy.checkpoint()
        $ quick_menu = True
        window show
        if _return == DRAW:
            show mateus sob with dissolve
            m "Oh não, foi um empate!"
            m "Estou muito triste..."
        else: # RESIGN or CHECKMATE
            $ winner = "White" if _return == WHITE else "Black"
            if player_color is not None: # PvC
                if _return == player_color:
                    show mateus grin with dissolve
                    m "Parabéns mor!! Estás a ficar cada vez melhor!"
                else:
                    show mateus grin with dissolve
                    m "HEHEHEHE GANHEI!"
        $ chess_subprocess.kill()        
        jump igor

    label igor:
        show mateus 2 with dissolve
        "Ficamos a falar mais um bocadinho."
        "Depois de algum tempo, o Igor chegou."
        play music "audio/igor dunas theme.mp3" fadeout 0.5 fadein 0.5
        show mateus 2 at right with dissolve
        show igor at left with dissolve
        m "Olha o Igor!"
        c "Olá Igor!"
        igor "Olá bro! Como é que estás?"
        m "Estou bem, e tu?"
        igor "Também bro! A tua chavalita é muita linda."
        m "Obrigado bro!"
        c "Obrigado Igor!"
        igor "Eu também tenho uma namorada, mas ela não é tão bonita como a tua."
        igor "Eu tenho trabalhado muito para ter o vinco e não tenho tido tempo para a ver."
        igor "Mas eu vou tentar arranjar tempo para a ver."
        m "Fazes bem em tentar, porque ela merece!"
        igor "Obrigado bro! Vocês já beberam alguma coisa?"
        m "Sim eu já! E a Constança também!"
        m "Mas estamos quase a ir embora."
        igor "Okay bro, a minha noite tá só a começar!"
        igor "Fica bem bro!"
        m "Adeus Igor!"
        c "Adeus Igor!"
        m "Vamos embora?"
        "Eu estava muito cansada, e conseguia ver que o Mateus também."
        c "Sim vamos, quero dormir muito agarradinha a ti!"
        jump dormir


    label dormir:
        scene casinha with dissolve
        "Eu e o Mateus chegamos a casinha dele."
        "Depois de passarmos algum tempo juntos, fomos dormir."
        show mateus grin
        m "Eu amo-te muito!"
        c "Também te amo!"
        m "Feliz dia dos namorados!"
        hide mateus grin
        show evil
        n "FIM!"
        hide evil
        "E assim acaba a nossa aventura."
return