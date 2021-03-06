"""
    bind_texture
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging
from OpenGL import GL
from mcedit2.rendering.scenegraph import rendernode
from mcedit2.rendering.scenegraph.rendernode import RenderstateRenderNode
from mcedit2.rendering.scenegraph.scenenode import Node
from mcedit2.util import glutils

log = logging.getLogger(__name__)


class BindTextureRenderNode(RenderstateRenderNode):
    def enter(self):
        GL.glPushAttrib(GL.GL_ENABLE_BIT | GL.GL_TEXTURE_BIT)
        scale = self.sceneNode.scale
        if scale is not None:
            GL.glMatrixMode(GL.GL_TEXTURE)
            GL.glPushMatrix()
            GL.glLoadIdentity()
            GL.glScale(*scale)
        glutils.glActiveTexture(GL.GL_TEXTURE0)  # disable texture1?
        GL.glEnable(GL.GL_TEXTURE_2D)
        if self.sceneNode.texture is not None:
            self.sceneNode.texture.bind()

    def exit(self):
        if self.sceneNode.scale is not None:
            # Please do not change BindTextureNode.scale during RenderNode calls, thx
            GL.glMatrixMode(GL.GL_TEXTURE)
            GL.glPopMatrix()
        GL.glPopAttrib()


class BindTextureNode(Node):
    RenderNodeClass = BindTextureRenderNode

    def __init__(self, texture, scale=None):
        """

        :type texture: glutils.Texture
        """
        super(BindTextureNode, self).__init__()
        self.texture = texture
        self.scale = scale
