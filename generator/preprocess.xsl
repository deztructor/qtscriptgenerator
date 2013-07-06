<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">

  <xsl:output method="xml" indent="yes"/>

  <xsl:param name="qt"/>
  <xsl:param name="arch"/>

  <xsl:template match="processing-instruction()" />

  <xsl:template match="@qt">
    <!-- skipped -->
  </xsl:template>

  <xsl:template match="@arch">
    <!-- skipped -->
  </xsl:template>

  <xsl:template match="@*">
    <xsl:copy>
      <xsl:apply-templates select="@*"/>
      <xsl:apply-templates select="node()"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="node()">
    <xsl:choose>
      <xsl:when test="count(@qt) = 0 or @qt = $qt">
        <xsl:apply-templates select="." mode="arch"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- skipped -->
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="node()" mode="arch">
    <xsl:choose>
      <xsl:when test="count(@arch) = 0">
        <xsl:copy>
          <xsl:apply-templates select="@*"/>
          <xsl:apply-templates select="node()"/>
        </xsl:copy>
      </xsl:when>
      <xsl:when test="starts-with(@arch, '!') and not(starts-with($arch, substring(@arch, 2)))">
        <xsl:copy>
          <xsl:apply-templates select="@*"/>
          <xsl:apply-templates select="node()"/>
        </xsl:copy>
      </xsl:when>
      <xsl:when test="starts-with($arch, @arch)">
        <xsl:copy>
          <xsl:apply-templates select="@*"/>
          <xsl:apply-templates select="node()"/>
        </xsl:copy>
      </xsl:when>
     <xsl:otherwise>
        <!-- skipped -->
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
