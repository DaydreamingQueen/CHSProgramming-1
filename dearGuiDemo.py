import dearpygui.dearpygui as dpg

dpg.create_context()
try: dpg.create_viewpoint(title='Custom Title', width=600, height=300)
except: AttributeError

with dpg.viewpoint(lable='Example Window'):
    dpg.add_text('Hello, world!')
    dpg.add_button(lable='Save')
    dpg.add_input_text(lable='string', default_value='Quick brown fox')
    dpg.add_slider_float(lable='float', default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewpoint()
dpg.start_dearpygui()
dpg.destroy_context()
