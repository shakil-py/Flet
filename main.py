import flet
from flet import *


def main(page: Page):
    bg = "#041955"
    fwg = "#97b4ff"
    fg = "#3450a1"
    pink = "#eb06ff"
    catagories_card = Row(
        scroll="auto"
    )
    catagories = ["Business", "Family", "Friends"]
    for i, catagory in enumerate(catagories):
        catagories_card.controls.append(
            Container(
                bgcolor=bg,
                height=110,
                width=170,
                border_radius=20,
                padding=15,
                content=Column(
                    controls=[
                        Text("40 Task"),
                        Text(catagory),
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white12",
                            border_radius=20,
                            padding=padding.only(right=i*30),
                            content=Container(
                                bgcolor="pink"
                            )
                        
                        )

                    ]
                )
            )
        )
    frist_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment="spaceBetween",
                    controls=[
                        Container(
                            content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]

                        )
                    ]
                    ),
                Text(
                    value="what\'s up shakil"),
                Text(
                    value="CATAGORIES"
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=catagories_card
                )
            ]
        )
    )
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=350,
                height=650,
                bgcolor=fg,
                border_radius=15,
                padding=padding.only(top=50, left=20, right=20, bottom=60),
                content=Column(
                    controls=[
                        frist_page_contents
                    ]
                )
            )
        ]
    )
    # main containear #######
    container = Container(
        width=350,
        height=650,
        bgcolor=bg,
        border_radius=15,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )

    )
    page.add(container)


app(target=main, host=WEB_BROWSER)
