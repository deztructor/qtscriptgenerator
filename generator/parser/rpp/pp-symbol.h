/****************************************************************************
**
** Copyright (C) 2008-2009 Nokia Corporation and/or its subsidiary(-ies).
** All rights reserved.
** Contact: Nokia Corporation (qt-info@nokia.com)
**
** This file is part of the Qt Script Generator project on Qt Labs.
**
** $QT_BEGIN_LICENSE:LGPL$
** No Commercial Usage
** This file contains pre-release code and may not be distributed.
** You may use this file in accordance with the terms and conditions
** contained in the Technology Preview License Agreement accompanying
** this package.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU Lesser General Public License version 2.1 requirements
** will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Nokia gives you certain additional
** rights.  These rights are described in the Nokia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** If you have questions regarding the use of this file, please contact
** Nokia at qt-info@nokia.com.
**
**
**
**
**
**
**
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef PP_SYMBOL_H
#define PP_SYMBOL_H

namespace rpp {

class pp_symbol
{
  static rxx_allocator<char> &allocator_instance ()
  {
    static rxx_allocator<char>__allocator;
    return __allocator;
  }
  static rxx_allocator<pp_fast_string> &ppfs_allocator_instance ()
  {
    static rxx_allocator<pp_fast_string>__ppfs_allocator;
    return __ppfs_allocator;
  }

public:
  static int &N()
  {
    static int __N;
    return __N;
  }

  static pp_fast_string const *get (char const *__data, std::size_t __size)
  {
    ++N();
    char *data = allocator_instance ().allocate (__size + 1);
    memcpy(data, __data, __size);
    data[__size] = '\0';

    pp_fast_string *where = ppfs_allocator_instance ().allocate (sizeof (pp_fast_string));
    return new (where) pp_fast_string (data, __size);
  }

  template <typename _InputIterator>
  static pp_fast_string const *get (_InputIterator __first, _InputIterator __last)
  {
    ++N();
    std::ptrdiff_t __size;
#if defined(__SUNPRO_CC)
    std::distance (__first, __last, __size);
#else
    __size = std::distance (__first, __last);
#endif
    assert (__size >= 0 && __size < 512);

    char *data = allocator_instance ().allocate (__size + 1);
    std::copy (__first, __last, data);
    data[__size] = '\0';

    pp_fast_string *where = ppfs_allocator_instance ().allocate (sizeof (pp_fast_string));
    return new (where) pp_fast_string (data, __size);
  }

  static pp_fast_string const *get(std::string const &__s)
  { return get (__s.c_str (), __s.size ()); }
};

} // namespace rpp

#endif // PP_SYMBOL_H

// kate: space-indent on; indent-width 2; replace-tabs on;
