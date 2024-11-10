import base64
import utils.utils as utils
from utils.utils import get_base64_encoded_image
import logging
# пути к картинкам банков
TBANK_IMAGE = 'mock_images/tbank.jpg'
YA_PAY_IMAGE = 'mock_images/ya_pay.jpg'
ALPHA_IMAGE = 'mock_images/alpha_logo.jpg'
SBER_IMAGE = 'mock_images/sber_logo.png'
VTB_IMAGE = 'mock_images/vtb_logo.jpg'

# пути к картинкам конкретных кешбэков
ASHAN_IMAGE = 'mock_images/ashan.jpg'
BRISTOL_IMAGE = 'mock_images/bristol.jpg'
DETMIR_IMAGE = 'mock_images/detmir.png'
FARSH_IMAGE = 'mock_images/farsh.png'
KASHA_IMAGE = 'mock_images/kasha.png'
KB_IMAGE = 'mock_images/kb.jpg'
KHLEB_IMAGE = 'mock_images/khleb.png'
LENTA_IMAGE = 'mock_images/lenta.png'
LETUAL_IMAGE = 'mock_images/letual.png'
MAGNIT_IMAGE = 'mock_images/magnit.jpg'
MASLO_IMAGE = 'mock_images/maslo.png'
MOLOKO_IMAGE = 'mock_images/moloko.png'
OLIVKOVOE_MASLO_IMAGE = 'mock_images/olivkovoe_maslo.png'
PEREKRESTOK_IMAGE = 'mock_images/perekrestok.png'
PODRUZHKA_IMAGE = 'mock_images/podruzhka.png'
POMODORO_IMAGE = 'mock_images/pomodoro.png'
PYATEROCHKA_IMAGE = 'mock_images/pyaterochka.png'
RIV_GOSH_IMAGE = 'mock_images/riv_gosh.png'
SAHAR_IMAGE = 'mock_images/sahar.png'
SMETANA_IMAGE = 'mock_images/smetana.png'
SOCHEN_IMAGE = 'mock_images/sochen.png'
SPAR_IMAGE = 'mock_images/spar.jpg'
TVOROG_IMAGE = 'mock_images/tvorog.png'
VINLAB_IMAGE = 'mock_images/vinlab.png'
VKUSVILL_IMAGE = 'mock_images/vkusvill.jpg'
YAYICA_IMAGE = 'mock_images/yayica.png'
ZOLOTOYE_YABLOKO_IMAGE = 'mock_images/zolotoye_yabloko.png'

# банковские идентификаторы
TBANK_BIK = 00000000
YA_PAY_BIK = 11111111
ALPHA_BIK = 22222222
SBER_BIK = 33333333
VTB_BIK = 44444444


def mock_search():
    # картинки с банками
    base64_tbank_image = get_base64_encoded_image(TBANK_IMAGE)
    base64_ya_pay_image = get_base64_encoded_image(YA_PAY_IMAGE)
    base64_alpha_image = get_base64_encoded_image(ALPHA_IMAGE)
    base64_sber_image = get_base64_encoded_image(SBER_IMAGE)
    base64_vtb_image = get_base64_encoded_image(VTB_IMAGE)

    # картинки с конкретными предложениями
    base64_ashan_image = get_base64_encoded_image(ASHAN_IMAGE)
    base64_bristol_image = get_base64_encoded_image(BRISTOL_IMAGE)
    base64_detmir_image = get_base64_encoded_image(DETMIR_IMAGE)
    base64_farsh_image = get_base64_encoded_image(FARSH_IMAGE)
    base64_kasha_image = get_base64_encoded_image(KASHA_IMAGE)
    base64_kb_image = get_base64_encoded_image(KB_IMAGE)
    base64_khleb_image = get_base64_encoded_image(KHLEB_IMAGE)
    base64_lenta_image = get_base64_encoded_image(LENTA_IMAGE)
    base64_letual_image = get_base64_encoded_image(LETUAL_IMAGE)
    base64_magnit_image = get_base64_encoded_image(MAGNIT_IMAGE)
    base64_maslo_image = get_base64_encoded_image(MASLO_IMAGE)
    base64_moloko_image = get_base64_encoded_image(MOLOKO_IMAGE)
    base64_olivkovoye_maslo_image = get_base64_encoded_image(OLIVKOVOE_MASLO_IMAGE)
    base64_perekrestok_image = get_base64_encoded_image(PEREKRESTOK_IMAGE)
    base64_podruzhka_image = get_base64_encoded_image(PODRUZHKA_IMAGE)
    base64_pomodoro_image = get_base64_encoded_image(POMODORO_IMAGE)
    base64_pyaterochka_image = get_base64_encoded_image(PYATEROCHKA_IMAGE)
    base64_riv_gosh_image = get_base64_encoded_image(RIV_GOSH_IMAGE)
    base64_sahar_image = get_base64_encoded_image(SAHAR_IMAGE)
    base64_smetana_image = get_base64_encoded_image(SMETANA_IMAGE)
    base64_sochen_image = get_base64_encoded_image(SOCHEN_IMAGE)
    base64_spar_image = get_base64_encoded_image(SPAR_IMAGE)
    base64_tvorog_image = get_base64_encoded_image(TVOROG_IMAGE)
    base64_vinlab_image = get_base64_encoded_image(VINLAB_IMAGE)
    base64_vkusvill_image = get_base64_encoded_image(VKUSVILL_IMAGE)
    base64_yayica_image = get_base64_encoded_image(YAYICA_IMAGE)
    base64_zolotoye_yabloko_image = get_base64_encoded_image(ZOLOTOYE_YABLOKO_IMAGE)

    result = [
        {
            'header': '10% на всё',
            'description': 'Кешбэк для всех новых пользователей до 32 октября',
            'category': 'Супермаркеты',
            'image': base64_ashan_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 300 рублей на красное вино',
            'description': 'Всем новым пользователям предоставляется скидка на первый заказ онлайн в сервисе Яндекс.Еда',
            'category': 'Супермаркеты',
            'image': base64_bristol_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 5% на настольные игры',
            'description': 'Получите кешбэк 5% на настольные игры! Покупайте любимые игры и возвращайте часть потраченных средств, чтобы обновить свою коллекцию',
            'category': 'Настольные игры',
            'image': base64_detmir_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк до 100% на говяжий фарш',
            'description': 'Верните полную стоимость при покупке от двух пачек',
            'category': 'Продукты',
            'image': base64_farsh_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 15% на овсянку',
            'description': 'Получите кешбэк 15% на овсянку! Наслаждайтесь полезным завтраком и экономьте на покупках',
            'category': 'Продукты',
            'image': base64_kasha_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 300 рублей на доставку',
            'description': 'Получите кешбэк 300 рублей на доставку! Заказывайте любимую еду и возвращайте часть средств обратно',
            'category': 'Супермаркеты',
            'image': base64_kb_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 22% на батоны',
            'description': 'Кешбэк 22% на батоны! Покупайте свежие батоны и возвращайте часть средств обратно!',
            'category': 'Продукты',
            'image': base64_khleb_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 200 рублей на сникерсы',
            'description': 'Кешбэк 200 рублей на сникерсы (при покупке 20 штук)! Наслаждайтесь любимыми сладостями и получайте выгоду от покупок!',
            'category': 'Супермаркеты',
            'image': base64_lenta_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 5% на красную помаду',
            'description': 'Кешбэк 5% на красную помаду! Придайте своим губам яркий оттенок и получайте выгоду от каждой покупки!',
            'category': 'Косметика',
            'image': base64_letual_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 100 рублей на туалетную бумагу',
            'description': 'Покупая туалетную бумагу, вы можете сэкономить! Получите кешбэк 100 рублей на эту необходимую продукцию и наслаждайтесь выгодными покупками!',
            'category': 'Супермаркеты',
            'image': base64_magnit_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 7% на подсолнечное масло Золотая Семечка',
            'description': 'Покупая подсолнечное масло Золотая Семечка, вы можете вернуть 7% от потраченной суммы. Сделайте свои покупки более выгодными и экономьте на каждом шагу',
            'category': 'Продукты',
            'image': base64_maslo_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 3% на пастеризованное молоко',
            'description': 'При покупке пастеризованного молока вы можете получить кешбэк в размере 3%. Это поможет вам сократить расходы на повседневные продукты',
            'category': 'Продукты',
            'image': base64_moloko_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 12% на оливковое масло',
            'description': 'При приобретении оливкового масла можно воспользоваться кешбэком в размере 12%. Это отличная возможность снизить затраты на покупку качественных продуктов',
            'category': 'Продукты',
            'image': base64_olivkovoye_maslo_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 4% на продукцию собственного производства',
            'description': 'При покупке продукции собственного производства вы можете получить кешбэк в размере 4%. Это может стать хорошим способом сэкономить на товарах, которые часто используются в повседневной жизни',
            'category': 'Супермаркеты',
            'image': base64_perekrestok_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 9% на тушь для ресниц',
            'description': 'Кешбэк в размере 9% доступен на тушь для ресниц. Это отличная возможность не только обновить свою косметичку, но и сэкономить на покупках',
            'category': 'Косметика',
            'image': base64_podruzhka_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 6% на помидоры',
            'description': 'Кешбэк в размере 6% предлагается на помидоры. Это замечательный способ поддержать здоровое питание и сэкономить на свежих овощах',
            'category': 'Продукты',
            'image': base64_pomodoro_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 8% на выпечку',
            'description': 'Кешбэк 8% на выпечку – отличный способ насладиться любимыми хлебобулочными изделиями и сэкономить на покупках',
            'category': 'Супермаркеты',
            'image': base64_pyaterochka_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 2% на крем для рук',
            'description': 'Кешбэк 2% на крем для рук – хорошая возможность ухаживать за кожей и получать небольшую выгоду от покупок',
            'category': 'Косметика',
            'image': base64_riv_gosh_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 60% на cахарный песок',
            'description': 'Кешбэк 60% на сахарный песок – отличная возможность сэкономить на покупке этого необходимого продукта',
            'category': 'Супермаркеты',
            'image': base64_sahar_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 13% на сметану',
            'description': 'Кешбэк 13% на сметану – хороший способ сэкономить на покупке этого вкусного и полезного продукта',
            'category': 'Продукты',
            'image': base64_smetana_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 80% на сочни с творогом',
            'description': 'Кешбэк 80% на сочни с творогом – это замечательная возможность насладиться вкусной выпечкой и значительно сэкономить на покупке! Не упустите шанс побаловать себя и своих близких!',
            'category': 'Продукты',
            'image': base64_sochen_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 200 рублей на спаржу',
            'description': 'Кешбэк 200 рублей на спаржу – отличное предложение для любителей этого полезного овоща! Это не только возможность сэкономить, но и шанс добавить в свой рацион вкусное и питательное блюдо.',
            'category': 'Супермаркеты',
            'image': base64_spar_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 40% на творог',
            'description': 'Кешбэк 40% на творог – отличная возможность приобрести этот полезный продукт и сэкономить! Творог богат белком и кальцием, что делает его прекрасным выбором для здорового питания. Не упустите шанс воспользоваться этим предложением!',
            'category': 'Продукты',
            'image': base64_tvorog_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 350 рублей на водку',
            'description': 'Кешбэк 350 рублей на водку – это заманчивое предложение для тех, кто планирует покупку этого напитка. Однако всегда стоит помнить о разумном потреблении алкоголя',
            'category': 'Продукты',
            'image': base64_vinlab_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 12% на фрукты',
            'description': 'Кешбэк 12% на фрукты – это отличная возможность сэкономить на покупке свежих и полезных продуктов! Фрукты богаты витаминами и минералами, и их стоит включать в свой рацион',
            'category': 'Супермаркеты',
            'image': base64_vkusvill_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 9% на яйца С0',
            'description': 'Кешбэк 9% на яйца — это хорошая возможность сэкономить на покупке этого полезного продукта. Яйца являются отличным источником белка и других питательных веществ',
            'category': 'Супермаркеты',
            'image': base64_yayica_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 700 рублей на средства для ухода за волосами',
            'description': 'Кешбэк 700 рублей на средства для ухода за волосами — это отличная возможность сэкономить на продуктах, которые помогут поддерживать здоровье и красоту ваших волос. Вы можете использовать этот кешбэк для покупки шампуней, кондиционеров, масок или стайлинговых средств',
            'category': 'Косметика',
            'image': base64_zolotoye_yabloko_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        }
    ]

    return result


def search(session: str, text):
    res = mock_search()

    if text is not None and len(text) > 0:
        res = utils.filter_response(text, res)

    return res

