#ifndef PixelROCTrimBits_h
#define PixelROCTrimBits_h
//
//
//

#include <fstream>
#include "CalibFormats/SiPixelObjects/interface/PixelROCName.h"
#include <string>

namespace pos{
  class PixelROCTrimBits {

  public:

    PixelROCTrimBits();

    void setROCTrimBits(PixelROCName rocid ,std::string bits);

    int read(PixelROCName rocid, std::ifstream& in);

    int readBinary(PixelROCName rocid, std::ifstream& in);

    friend std::ostream& operator<<(std::ostream& s, const PixelROCTrimBits& trimbits);

    unsigned int trim(unsigned int col, unsigned int row) const;

    void setTrim(unsigned int col, unsigned int row, unsigned int trim);

    void writeBinary(std::ofstream& out) const;

    void writeASCII(std::ofstream& out) const;

    PixelROCName name() const {return rocid_;}

  private:

    unsigned char bits_[2080];
    PixelROCName rocid_;


  };

}
#endif
