cmake_minimum_required(VERSION 3.18)
project(TODO_your_project_name VERSION 1.0)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wconversion")
include(CTest)

set(CPP_SRCS  # TODO: add all source files
  main.cpp
  file1.cpp
  ... .cpp
)

find_package(wxWidgets REQUIRED COMPONENTS net core base)
if(wxWidgets_USE_FILE) # not defined in CONFIG mode
    include(${wxWidgets_USE_FILE})
endif()

add_executable(${PROJECT_NAME} ${CPP_SRCS})
target_link_libraries(${PROJECT_NAME} ${wxWidgets_LIBRARIES})
