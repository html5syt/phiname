import flet as ft

from flet_contrib.color_picker import ColorPicker

# customColor = "#FFFFFF"
# nick=None


# """
# [colorPicker]
# """
# import colorsys

# # import flet_core as ft

# from hue_slider import HueSlider
# from utils import *

# # import main

# COLOR_MATRIX_WIDTH = 340
# CIRCLE_SIZE = 20


# # class ColorPicker(ft.Column):
# #     def __init__(self, color="#000000", width=COLOR_MATRIX_WIDTH):
# #         super().__init__()
# #         self.tight = True
# #         self.width = width
# #         self.__color = color
# #         self.hue_slider = HueSlider(
# #             on_change_hue=self.update_color_picker_on_hue_change,
# #             hue=hex2hsv(self.color)[0],
# #         )
# #         self.generate_color_map()
# #         self.generate_selected_color_view()

# #     # color
# #     @property
# #     def color(self):
# #         return self.__color

# #     @color.setter
# #     def color(self, value):
# #         self.__color = value

# #     def before_update(self):
# #         super().before_update()
# #         # called every time on self.update()
# #         self.hue_slider.hue = hex2hsv(self.color)[0]
# #         self.update_circle_position()
# #         self.update_color_map()
# #         self.update_selected_color_view_values()

# #     def update_circle_position(self):
# #         hsv_color = hex2hsv(self.color)
# #         self.thumb.left = hsv_color[1] * self.color_map.width  # s * width
# #         self.thumb.top = (1 - hsv_color[2]) * self.color_map.height  # (1-v)*height

# #     def find_color(self, x, y):
# #         h = self.hue_slider.hue
# #         s = x / self.color_map.width
# #         v = (self.color_map.height - y) / self.color_map.height
# #         self.color = rgb2hex(colorsys.hsv_to_rgb(h, s, v))

# #     def generate_selected_color_view(self):
# #         rgb = hex2rgb(self.color)

# #         def on_hex_submit(e):
# #             global customColor
# #             try:
# #                 self.color = e.control.value
# #             except:
# #                 customColor = self.color
# #                 custom_color(self.color)
# #             self.update()

# #         def __on_rgb_submit():
# #             rgb = (
# #                 int(self.r.value) / 255,
# #                 int(self.g.value) / 255,
# #                 int(self.b.value) / 255,
# #             )
# #             self.color = rgb2hex(rgb)

# #         def on_rgb_submit(e):
# #             __on_rgb_submit()
# #             self.update()

# #         self.hex = ft.TextField(
# #             label="Hex",
# #             text_size=12,
# #             value=self.__color,
# #             height=40,
# #             width=90,
# #             on_submit=on_hex_submit,
# #             on_blur=on_hex_submit,
# #         )
# #         self.r = ft.TextField(
# #             label="R",
# #             height=40,
# #             width=55,
# #             value=rgb[0],
# #             text_size=12,
# #             on_submit=on_rgb_submit,
# #             on_blur=on_rgb_submit,
# #         )
# #         self.g = ft.TextField(
# #             label="G",
# #             height=40,
# #             width=55,
# #             value=rgb[1],
# #             text_size=12,
# #             on_submit=on_rgb_submit,
# #             on_blur=on_rgb_submit,
# #         )
# #         self.b = ft.TextField(
# #             label="B",
# #             height=40,
# #             width=55,
# #             value=rgb[2],
# #             text_size=12,
# #             on_submit=on_rgb_submit,
# #             on_blur=on_rgb_submit,
# #         )
# #         self.selected_color_view = ft.Column(
# #             spacing=20,
# #             controls=[
# #                 ft.Row(
# #                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
# #                     controls=[
# #                         ft.Container(
# #                             width=30, height=30, border_radius=30, bgcolor=self.__color
# #                         ),
# #                         self.hue_slider,
# #                     ],
# #                 ),
# #                 ft.Row(
# #                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
# #                     controls=[
# #                         self.hex,
# #                         self.r,
# #                         self.g,
# #                         self.b,
# #                     ],
# #                 ),
# #                 self.submit,
# #             ],
# #         )

# #         self.controls.append(self.selected_color_view)

# #     def update_selected_color_view_values(self):
# #         rgb = hex2rgb(self.color)
# #         self.selected_color_view.controls[0].controls[
# #             0
# #         ].bgcolor = self.color  # Colored circle
# #         self.hex.value = self.__color  # Hex
# #         self.r.value = rgb[0]  # R
# #         self.g.value = rgb[1]  # G
# #         self.b.value = rgb[2]  # B
# #         self.thumb.bgcolor = self.color  # Color matrix circle

# #     def generate_color_map(self):
# #         def __move_circle(x, y):
# #             self.thumb.top = max(
# #                 0,
# #                 min(
# #                     y - CIRCLE_SIZE / 2,
# #                     self.color_map.height,
# #                 ),
# #             )
# #             self.thumb.left = max(
# #                 0,
# #                 min(
# #                     x - CIRCLE_SIZE / 2,
# #                     self.color_map.width,
# #                 ),
# #             )
# #             self.find_color(x=self.thumb.left, y=self.thumb.top)
# #             self.update_selected_color_view_values()

# #         def on_pan_update(e: ft.DragStartEvent):
# #             __move_circle(x=e.local_x, y=e.local_y)
# #             self.selected_color_view.update()
# #             self.thumb.update()

# #         self.color_map_container = ft.GestureDetector(
# #             content=ft.Stack(
# #                 width=self.width,
# #                 height=int(self.width * 3 / 5),
# #             ),
# #             on_pan_start=on_pan_update,
# #             on_pan_update=on_pan_update,
# #         )

# #         saturation_container = ft.Container(
# #             gradient=ft.LinearGradient(
# #                 begin=ft.alignment.center_left,
# #                 end=ft.alignment.center_right,
# #                 colors=[ft.colors.WHITE, ft.colors.RED],
# #             ),
# #             width=self.color_map_container.content.width - CIRCLE_SIZE,
# #             height=self.color_map_container.content.height - CIRCLE_SIZE,
# #             border_radius=5,
# #         )

# #         self.color_map = ft.ShaderMask(
# #             top=CIRCLE_SIZE / 2,
# #             left=CIRCLE_SIZE / 2,
# #             content=saturation_container,
# #             blend_mode=ft.BlendMode.MULTIPLY,
# #             shader=ft.LinearGradient(
# #                 begin=ft.alignment.top_center,
# #                 end=ft.alignment.bottom_center,
# #                 colors=[ft.colors.WHITE, ft.colors.BLACK],
# #             ),
# #             border_radius=5,
# #             width=saturation_container.width,
# #             height=saturation_container.height,
# #         )

# #         self.thumb = ft.Container(
# #             width=CIRCLE_SIZE,
# #             height=CIRCLE_SIZE,
# #             border_radius=CIRCLE_SIZE,
# #             border=ft.border.all(width=2, color="white"),
# #         )

# #         self.color_map_container.content.controls.append(self.color_map)
# #         self.color_map_container.content.controls.append(self.thumb)
# #         self.controls.append(self.color_map_container)

# #     def update_color_map(self):
# #         h = self.hue_slider.hue
# #         s = hex2hsv(self.color)[1]
# #         v = hex2hsv(self.color)[2]
# #         container_gradient_colors = [
# #             rgb2hex(colorsys.hsv_to_rgb(h, 0, 1)),
# #             rgb2hex(colorsys.hsv_to_rgb(h, 1, 1)),
# #         ]

# #         self.color_map.content.gradient.colors = container_gradient_colors

# #         self.color = rgb2hex(colorsys.hsv_to_rgb(h, s, v))

# #     def update_color_picker_on_hue_change(self):
# #         self.update_color_map()
# #         self.update_selected_color_view_values()
# #         self.selected_color_view.update()
# #         self.color_map_container.update()


# """
# [END]
# """


# # 设置自定义颜色
# def custom_color(hex):
#     global customColor
#     customColor = hex
#     print(customColor)


def main(page: ft.Page):
    # global nick

    # 单一事件
    # 导航栏
    def navigationTo(e: ft.ControlEvent):
        nonlocal navigation
        navigation = e.data
        # print(navigation)

    page.adaptive = True  # 自适应
    page.fonts = {
        "logo": "/tittle.ttf",
        "text": "/text.ttf",
    }  # 字体
    page.theme = ft.Theme(font_family="text")
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.scroll = ft.ScrollMode.AUTO
    # 页眉/页脚
    if (
        page.platform == ft.PagePlatform.WINDOWS
        or page.platform == ft.PagePlatform.MACOS
        or page.platform == ft.PagePlatform.LINUX
    ):
        page.appbar = ft.AppBar(
            adaptive=True,
            leading=ft.Image(
                src=f"/icon.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                offset=ft.transform.Offset(x=0.2, y=0),
            ),
            leading_width=35,
            title=ft.Text(
                spans=[
                    ft.TextSpan(
                        "Phigros 彩色昵称生成器",
                        ft.TextStyle(
                            # size=20,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    begin=ft.Offset(x=0, y=0),
                                    end=ft.Offset(x=350, y=0),
                                    color_stops=[
                                        0.125,
                                        0.250,
                                        0.375,
                                        0.5,
                                        0.625,
                                        0.75,
                                        0.875,
                                    ],
                                    colors=[
                                        ft.colors.RED,
                                        ft.colors.ORANGE,
                                        ft.colors.YELLOW,
                                        ft.colors.GREEN,
                                        ft.colors.BLUE,
                                        ft.colors.INDIGO,
                                        ft.colors.PURPLE,
                                    ],
                                )
                            ),
                            shadow=ft.BoxShadow(
                                offset=ft.Offset(x=0, y=0),
                                blur_radius=20,
                                color=ft.colors.BLUE,
                            ),
                            # color=ft.colors.WHITE,
                        ),
                    ),
                ],
                text_align=ft.TextAlign.CENTER,
                font_family="logo",
            ),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.BRIGHTNESS_AUTO, on_click=lambda _: dark_mode()),
                # ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="关于", on_click=lambda _: delc(nick)),
                        ft.PopupMenuItem(text="作者のB站"),
                    ]
                ),
            ],
        )
    else:
        page.appbar = ft.AppBar(
            adaptive=True,
            leading=ft.Image(
                src=f"/icon.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                offset=ft.transform.Offset(x=0.3, y=0),
            ),
            leading_width=35,
            title=ft.Text(
                spans=[
                    ft.TextSpan(
                        "Phigros 彩色昵称生成器",
                        ft.TextStyle(
                            size=15,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    begin=ft.Offset(x=0, y=0),
                                    end=ft.Offset(x=350, y=0),
                                    color_stops=[
                                        0.125,
                                        0.250,
                                        0.375,
                                        0.5,
                                        0.625,
                                        0.75,
                                        0.875,
                                    ],
                                    colors=[
                                        ft.colors.RED,
                                        ft.colors.ORANGE,
                                        ft.colors.YELLOW,
                                        ft.colors.GREEN,
                                        ft.colors.BLUE,
                                        ft.colors.INDIGO,
                                        ft.colors.PURPLE,
                                    ],
                                )
                            ),
                            shadow=ft.BoxShadow(
                                offset=ft.Offset(x=0, y=0),
                                blur_radius=20,
                                color=ft.colors.BLUE,
                            ),
                            # color=ft.colors.WHITE,
                        ),
                    ),
                ],
                text_align=ft.TextAlign.CENTER,
                font_family="logo",
            ),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.BRIGHTNESS_AUTO, on_click=lambda _: dark_mode()),
                # ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="关于", on_click=lambda _: delc(nick)),
                        ft.PopupMenuItem(text="作者のB站"),
                    ]
                ),
            ],
        )
    page.navigation_bar = ft.NavigationBar(
        adaptive=True,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.INVERT_COLORS, label="单色"),
            ft.NavigationBarDestination(icon=ft.icons.FORMAT_COLOR_FILL, label="多色"),
            ft.NavigationBarDestination(
                icon=ft.icons.COLOR_LENS_OUTLINED,
                selected_icon=ft.icons.COLOR_LENS,
                label="渐变",
            ),
        ],
        on_change=navigationTo,
    )

    navigation = 0

    # 自定义（事件）函数
    # 深色模式
    def dark_mode():
        # print(page.theme_mode)
        if page.theme_mode == ft.ThemeMode.SYSTEM:
            page.theme_mode = ft.ThemeMode.DARK
            page.appbar.actions[0].icon = ft.icons.DARK_MODE
            page.update()
        elif page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.appbar.actions[0].icon = ft.icons.WB_SUNNY_OUTLINED
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.SYSTEM
            page.appbar.actions[0].icon = ft.icons.BRIGHTNESS_AUTO
            page.update()

    # 删除元素
    def delc(e):
        page.controls.remove(e)
        # e.visible = False
        page.update()

    # 复制文本
    def copy(e):
        page.set_clipboard(copytext.value)
        page.overlay.append(
            ft.SnackBar(
                content=ft.Text("结果已复制到剪贴板！"), open=True, duration=2000
            )
        )
        page.update()

    # 颜色处理
    def colorProssing(e:ft.ControlEvent, color=None):
        nonlocal navigation, copytext, size,colors
        # print("navigation:",navigation)
        # 单色部分
        if int(navigation) == 0:
            print(e.control)
            resultTmp = nick[0].value
            if bold.value:
                resultTmp = f"<b>{resultTmp}</b>"
            if itatic.value:
                resultTmp = f"<i>{resultTmp}</i>"
            try:
                if ("字号" == e.control.label and size.value != "0"):
                    try:
                        if float(size.value) !=0:
                            size.error_text = ""
                            resultTmp = f"<size={size.value}>{resultTmp}</size>"
                    except:
                        size.error_text = "请输入正确的数字！"
            except:
                if size.value != "0" or size.value != None:
                    # print("size:", type(float(size.value)))
                    try:
                        if float(size.value) !=0:
                            size.error_text = ""
                            resultTmp = f"<size={size.value}>{resultTmp}</size>"
                    except:
                        size.error_text = "请输入正确的数字！"
            for key,value in {"红色":"red", "橙色":"orange", "黄色":"yellow", "绿色":"green", "蓝色":"blue","靛色":"#4b0082", "紫色":"purple", }.items():
                if colors.value == key:
                    resultTmp = f"<color={value}>{resultTmp}</color>"
                
        copytext.value = f"{resultTmp}\nGearnerated by PhiName"
        page.update()

    color=""

    # 颜色列表更改事件
    def color_change(e):
        nonlocal color
        tmp = ft.ResponsiveRow(
            [
                ft.Column(
                    col={"xxl": 3, "xl": 4, "lg": 4, "md": 6, "sm": 6, "xs": 12},
                    controls=[color_picker],
                ),
                ft.Column(
                    col={"xxl": 9, "xl": 8, "lg": 8, "md": 6, "sm": 6, "xs": 12},
                    controls=[result],
                ),
            ],
            columns=12,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        if colors.value == "自选颜色":
            if (
                page.platform == ft.PagePlatform.WINDOWS
                or page.platform == ft.PagePlatform.MACOS
                or page.platform == ft.PagePlatform.LINUX
            ):
                delc(result)
                copytext.expand = True
                copytext.min_lines = 1
                copytext.max_lines = 12
                copytext.width = 1000
                # tmp.scroll = ft.ScrollMode.AUTO
                page.add(tmp)
            else:
                delc(result)
                page.add(tmp)
        else:
            if (
                page.platform == ft.PagePlatform.WINDOWS
                or page.platform == ft.PagePlatform.MACOS
                or page.platform == ft.PagePlatform.LINUX
            ):
                # print(tmp)
                # 死BUG滚啊啊啊！
                # color_picker.visible = False
                page.controls.pop()
                copytext.expand = True
                copytext.min_lines = 1
                copytext.max_lines = 11
                page.add(result)
                # fo
            else:
                delc(tmp)
                copytext.expand = True
                page.add(result)
                # page.update()

    # 组件
    # 公用

    nick = (
        ft.TextField(
            adaptive=True,
            label="请输入昵称",
            hint_text="请输入昵称...",
            on_change=colorProssing,
        ),
    )

    bold = ft.Switch(label="加粗 ", value=False, adaptive=True, on_change=colorProssing)
    itatic = ft.Switch(
        label="斜体", value=False, adaptive=True, on_change=colorProssing
    )
    size = ft.TextField(
        adaptive=True,
        label="字号",
        expand=True,
        on_change=colorProssing,
        helper_text="仅限数字，0为默认大小",
        value=0,
    )
    copytext = ft.TextField(
        adaptive=True,
        label="结果",
        helper_text="Tips: 复制所有内容到Phigros的名字框中，完成后直接退出设置界面咕~",
        multiline=True,
        min_lines=1,
        max_lines=5,
        expand=True,
    )
    # preview = ft.Row([copytext, ft.IconButton(ft.icons.COPY_OUTLINED)])
    preview = ft.Container(
        content=ft.Text(
            "",
            size=30,
            text_align=ft.TextAlign.RIGHT,
            # expand=True,
            color=ft.colors.WHITE,
            font_family="text",
            spans=[
                ft.TextSpan(
                    "here goes italic",
                    ft.TextStyle(italic=True, size=20, color=ft.colors.GREEN),
                    spans=[
                        ft.TextSpan(
                            "bold and italic顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶ffdsdfghfdfsfsfgssgsgdsgsdgsdgsdgdgs",
                            ft.TextStyle(weight=ft.FontWeight.BOLD),
                        ),
                        ft.TextSpan(
                            "just italic",
                            spans=[
                                ft.TextSpan("smaller italic", ft.TextStyle(size=15))
                            ],
                        ),
                    ],
                )
            ],
        ),
        bgcolor=ft.colors.BLACK,
    )
    result = ft.Column(
        [
            ft.Row([copytext, ft.IconButton(ft.icons.COPY_OUTLINED, on_click=copy)]),
            ft.Row(
                [
                    ft.Text("预览：", weight=ft.FontWeight.BOLD, size=30),
                    preview,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
        ]
    )

    # 单色/多色
    colors = ft.Dropdown(
        label="颜色",
        hint_text="选择您喜欢的颜色...",
        on_change=color_change,
        options=[
            ft.dropdown.Option("红色",on_click=colorProssing),
            ft.dropdown.Option("橙色",on_click=colorProssing),
            ft.dropdown.Option("黄色",on_click=colorProssing),
            ft.dropdown.Option("绿色",on_click=colorProssing),
            ft.dropdown.Option("蓝色",on_click=colorProssing),
            ft.dropdown.Option("靛色",on_click=colorProssing),
            ft.dropdown.Option("紫色",on_click=colorProssing),
            ft.dropdown.Option("自选颜色"),
        ],
    )
    color_picker_ctrl = ColorPicker(color="#c8df6f")
    color_picker = ft.Column(
        controls=[
            color_picker_ctrl,
            ft.FilledButton(
                "设置颜色",
                adaptive=True,
                on_click=colorProssing,
                width=color_picker_ctrl.width,
            ),
        ],
        # alignment=ft.MainAxisAlignment.CENTER,
    )

    # CP = ft.Row([color_picker], alignment=ft.MainAxisAlignment.SPACE_AROUND, wrap=True,scroll=True)

    page.add(
        nick[0],
        ft.Divider(),
        colors,
        ft.Row(
            [bold, itatic, ft.VerticalDivider(), size],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        ),
        ft.Divider(),
        result,
    )


ft.app(
    target=main,
    web_renderer=ft.WebRenderer.HTML,
    assets_dir="assets",
)
