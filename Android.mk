LOCAL_PATH:= $(call my-dir)

include $(CLEAR_VARS)

LOCAL_SRC_FILES := cCtypeLib.c kivyTestCtype.py
LOCAL_MODULE_TAGS := eng
LOCAL_MODULE := libcCtypeLib
include $(BUILD_SHARED_LIBRARY)
#	$(shell mkdir -p $(TARGET_OUT)/system/share/kivy-examples)
#	$(shell cp -v   $(LOCAL_PATH)/kivyTestCtype.py $(TARGET_OUT)/system/share/kivy-examples)

include $(CLEAR_VARS)
LOCAL_MODULE := kivyTestCtype.py
LOCAL_MODULE_CLASS := ETC
LOCAL_MODULE_PATH := $(TARGET_OUT)/system/share/kivy-examples
LOCAL_SRC_FILES := $(LOCAL_MODULE)
LOCAL_MODULE_TAGS := eng
include $(BUILD_PREBUILT)


