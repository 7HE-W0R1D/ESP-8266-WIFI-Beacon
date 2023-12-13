#ifdef __has_include
    #if __has_include("lvgl.h")
        #ifndef LV_LVGL_H_INCLUDE_SIMPLE
            #define LV_LVGL_H_INCLUDE_SIMPLE
        #endif
    #endif
#endif

#if defined(LV_LVGL_H_INCLUDE_SIMPLE)
    #include "lvgl.h"
#else
    #include "lvgl/lvgl.h"
#endif


#ifndef LV_ATTRIBUTE_MEM_ALIGN
#define LV_ATTRIBUTE_MEM_ALIGN
#endif

#ifndef LV_ATTRIBUTE_IMG_NETWORK_PING_FILL0_WGHT400_GRAD0_OPSZ20
#define LV_ATTRIBUTE_IMG_NETWORK_PING_FILL0_WGHT400_GRAD0_OPSZ20
#endif

const LV_ATTRIBUTE_MEM_ALIGN LV_ATTRIBUTE_LARGE_CONST LV_ATTRIBUTE_IMG_NETWORK_PING_FILL0_WGHT400_GRAD0_OPSZ20 uint8_t network_ping_FILL0_wght400_GRAD0_opsz20_map[] = {
  0x00, 0x00, 0x00, 0x02, 	/*Color of index 0*/
  0x00, 0x00, 0x00, 0xd7, 	/*Color of index 1*/

  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x30, 0x03, 0xc0, 
  0x18, 0x03, 0xc0, 
  0x0c, 0x03, 0xc0, 
  0x06, 0x07, 0x00, 
  0x03, 0x0c, 0x00, 
  0x01, 0x98, 0x00, 
  0x00, 0xf0, 0x00, 
  0x0a, 0xfa, 0x00, 
  0x0f, 0xff, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 
};

const lv_img_dsc_t network_ping_FILL0_wght400_GRAD0_opsz20 = {
  .header.cf = LV_IMG_CF_INDEXED_1BIT,
  .header.always_zero = 0,
  .header.reserved = 0,
  .header.w = 20,
  .header.h = 20,
  .data_size = 68,
  .data = network_ping_FILL0_wght400_GRAD0_opsz20_map,
};
