import dearpygui.dearpygui as dpg

def run_app():
  dpg.create_context()
  width, height, channels, data = dpg.load_image("image.jpg")
  with dpg.texture_registry(show=True):
      dpg.add_static_texture(width=width, height=height, default_value=data, tag="testimage")

  with dpg.window(label="Image viewer 0.0.1"):
      dpg.add_image("testimage")


  dpg.create_viewport(title='Custom Title', width=800, height=600)
  dpg.setup_dearpygui()
  dpg.show_viewport()
  dpg.start_dearpygui()
  dpg.destroy_context()

# ##########

# import dearpygui.dearpygui as dpg

# def save_callback():
#     print("Save Clicked")

# def run_app():
#   dpg.create_context()
#   dpg.create_viewport()
#   dpg.setup_dearpygui()

#   with dpg.window(label="Example Window"):
#       dpg.add_text("Hello world")
#       dpg.add_button(label="Save", callback=save_callback)
#       dpg.add_input_text(label="string")
#       dpg.add_slider_float(label="float")

#   dpg.show_viewport()
#   dpg.start_dearpygui()
#   dpg.destroy_context()


if __name__ == "__main__":
  run_app()