import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='demo screen',width=300,height=400)

dpg.setup_dearpygui()
dpg.show_viewpoint()
dpg.start_dearpygui()
dpg.destroy_context()
