#pragma once

#include <string>

class Text {
public:
    Text(const std::string& text);
    std::string getText();

private:
  std::string text;
};
