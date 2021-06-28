import java.util.map

def checkoutScm(Map config) {
    String scmUrl = config.get(pScmUrl).trim()
    String scmBranch = config.get(pScmBranch).trim()
    String dstDir = config.get(pBaseDir).trim()
    dir(dstDir) {
        git url: scmUrl,
            branch: scmBranch,
  }
}

return this
